import torch
import torchvision
from thop import profile
model = torchvision.models.resnet18()
    # input = torch.randn(1, 3, 224, 224)
input = torch.randn(1, 3, 224, 224)

macs, params = profile(model, inputs=(input, ))