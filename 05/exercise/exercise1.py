from PIL import Image
from pathlib import Path
from torch.utils.data import Dataset, DataLoader
import glob

data_directory = "./data"
data_directory_path = Path(data_directory).resolve()
print("---1---")
print("---Displaying the absolute path---")
print(data_directory_path)

file_list = list(data_directory_path.glob("*"))
print("---2---")
print("---Display all files underneath---")
for file_list in file_list:
    print(file_list)

file_num = 0
for i in range(len(file_list)):
    count += 1
print("---3---")
print("file_num = ")
print(file_num)

