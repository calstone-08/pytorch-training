import torch
import numpy as np

data = np.array([
[[85, 78], [67, 82], [92, 88], [75, 70], [60, 64]],
[[70, 68], [77, 72], [85, 90], [60, 65], [78, 76]],
[[80, 84], [88, 87], [66, 68], [72, 73], [64, 60]]])

print("=== problem1 ===")
data_trc = torch.tensor(data)
print(torch.Tensor.size(data_trc))
print("=== problem2 ===")
data_trc2 = torch.permute(data_trc,(2,0,1))
print(data_trc2)
print(torch.Tensor.size(data_trc2))
print("=== problem3 ===")
sum_subj = torch.sum(data_trc2, axis = 0)
print(sum_subj)
print("=== problem4 ===")
ave_class = torch.mean(sum_subj, dtype=float, axis = 1)
print(ave_class)
print("=== problem5 ===")
ave_class2 = torch.zeros(1,3)
ave_class2[0,0] = torch.sum(ave_class[0], axis=0)
ave_class2[0,1] = torch.sum(ave_class[1], axis=0)
ave_class2[0,2] = torch.sum(ave_class[2], axis=0)
print(ave_class2)
