import numpy as np

np.transpose
N=2
H=3
W=4
C=5
a=np.arange(120).reshape(N,H,W,C)
print(a.transpose(0,3,1,2).shape)
# N C H W