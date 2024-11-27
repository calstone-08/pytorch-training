import matplotlib.pyplot as plt
from PIL import Image
from torchvision import transforms

preprocess_1 = transforms.Compose([
    transforms.Resize((213,320)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5,0.5,0.5], std=[0.5,0.5,0.5])

])

image_path = "./exercise_data/dog_img.png"
image = Image.open(image_path)
processed_image = preprocess_1(image)
print("変更前の画像サイズ")
print(image.size)
print("変更後の画像サイズ")
print(processed_image.shape[1],processed_image.shape[2])
plt.imshow(processed_image.permute(1,2,0))
plt.show