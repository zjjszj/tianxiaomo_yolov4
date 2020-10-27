import torch

a=torch.rand(1,2,3,4,5)
print(a.shape)
print(a[..., :3].shape)