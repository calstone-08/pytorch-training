import numpy as np

data = np.array([
    [[65,70], [56,80],[78,68],[90,85],[60,75]],
    [[70,75],[54,88],[82,64],[88,83],[58,78]],
    [[67,72],[52,82],[80,66],[86,80],[59,74]]])

print("array size ", data.shape)
print(np.mean(data, axis = 1))
print(np.max(data[2,:,:]))
np.max(data)
print(data[data>80].shape[0])
print(data[data.sum(axis=2)>135].shape[0])