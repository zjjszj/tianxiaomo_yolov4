import torch
from torchvision.models.resnet import resnet18

def collate_fn(batch):
    return tuple(zip(*batch))

print(collate_fn([(1,2),(3,4),(5,6)]))