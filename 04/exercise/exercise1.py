import torch
from torch import nn


if __name__=="__main__":
    my_tensor = torch.ones(32, 3, 128, 128)

    conv = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3)
    conv2 = nn.Conv2d(in_channels=3, out_channels=256, kernel_size=3, stride=2, padding=1)
    conv3 = nn.Conv2d(in_channels=3, out_channels=256, kernel_size=5, stride=2, padding=2)
    


    out = conv(my_tensor)
    print(repr(out.size()))

    out2 = conv2(my_tensor)
    print(repr(out2.size()))

    out3 = conv3(my_tensor)
    print(repr(out3.size()))
    