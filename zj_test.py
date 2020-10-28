import numpy as np


a=[]
a1=np.random.random((1,2,3))
a2=np.random.random((1,2,3))
a.append(a1)
a.append(a2)
b=np.concatenate(a, axis=0)
print(b.shape)