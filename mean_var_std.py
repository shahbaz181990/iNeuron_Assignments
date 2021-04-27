import numpy as np

def calculate(list):
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.ValueError")
  

  n = np.array(list).reshape(3,3)
    
  mean = [(np.mean(n,axis=0)).tolist(),(np.mean(n,axis=1)).tolist(),np.mean(n)]
    

  variance = [(np.var(n,axis=0)).tolist(),(np.var(n,axis=1)).tolist(),np.var(n)]
    
  std_dev = [(np.std(n,axis=0)).tolist(),(np.std(n,axis=1)).tolist(),np.std(n)]
     
  maximum = [(np.max(n,axis=0)).tolist(),(np.max(n,axis=1)).tolist(),np.max(n)]
 
  minimum = [(np.min(n,axis=0)).tolist(),(np.min(n,axis=1)).tolist(),np.min(n)]

  tot_sum = [(np.sum(n,axis=0)).tolist(),(np.sum(n,axis=1)).tolist(),np.sum(n)]

    
  calculations = {'mean' : mean,
             'variance' : variance,
             'standard deviation' : std_dev,
             'max' : maximum,
             'min' : minimum,
             'sum' : tot_sum
             }




  return calculations