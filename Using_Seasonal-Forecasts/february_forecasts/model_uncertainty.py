def mix_norm_cdf(x,means,std,weights=-1) :
#   calculate  cdf(x) of a mixture of normal distributions with
#   means: an array containing the mean of each distributions
#   std: an array len(means) containing the std deviation of each normal _or_
#        a single value which is a common standard deviation for each normal
#   weights: an optional array of len(means) of the weights for each normal
#        if sum(weights) != 1 then it's normalized to 1
#   There is currently no code to test for len(weights)=len(std)=len(means)
    import numpy as np
    from scipy.stats import norm
    
    if np.size(weights) == 1 :
        weights=np.full(len(means),1.0/len(means))
    if np.sum(weights) - 1 > 1.e-4 :
        print('!!! Warning ')
        print('Sum of weights =',np.sum(weights),' Normalizing to 1')
        weights=weights/np.sum(weights)
    if np.size(std) == 1 :
        std=np.full(len(means),std)

    mcdf=0.0
    for i in range(len(means)) :
        mcdf += weights[i]*norm.cdf(x,loc=means[i],scale=std[i])

    return mcdf

def mix_norm_ppf(p,means,std,weights=-1,tol=1.e-4) :
# routine to estimate a quantile for mixture of normals given by mix_norm_cdf
# p should be given as a probability i.e. p in [0,1]
    import numpy as np
    from scipy.stats import norm

    if weights == -1 :
        weights=np.full(len(means),1.0/len(means))
    if np.size(std) == 1 :
        std=np.full(len(means),std)
        

    x=np.percentile(means,p*100)
    f=mix_norm_cdf(x,means,std)
    i=0
    while np.abs(p-f) > tol :
        i=i+1
        df=(mix_norm_cdf(x+0.01,means,std,weights=weights)-f)/0.01
#        print(i,x,f,df,p-f)
        x=x+(p-f)/df
        f=mix_norm_cdf(x,means,std,weights=weights)

#    print(x,f)
    return(x)

