# 方法一
# 将若干张图片拼成一张图片展示
# 展示出来的图片的宽度：nrow, 高度：len(imge)/nrow
import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import torchvision
import matplotlib.pyplot as plt


def image_show(images):
    images = images.numpy()
    images = images.transpose((1, 2, 0))
    print(images.shape)
    plt.imshow(images)
    plt.show()


def main():
    train_dataset = datasets.MNIST(root='./datasets', train=False, download=True,
                                   transform=transforms.ToTensor())
    train_loader = DataLoader(train_dataset, batch_size=4, shuffle=False)

    device = torch.device('cuda:0')
    # for batch_idx, (inputs, targets) in enumerate(train_loader):
    #     inputs = inputs.to(device)
    #     print(inputs.shape)
    inputs, targets = next(iter(train_loader))
    print(inputs.shape)
    print(targets.shape)

    images = torchvision.utils.make_grid(inputs)
    print(f'images.shape:{images.shape}')
    image_show(images)


if __name__ == '__main__':
    main()



# 方法二
# sphinx_gallery_thumbnail_path = "../../gallery/assets/visualization_utils_thumbnail2.png"

import torch
import numpy as np
import matplotlib.pyplot as plt

import torchvision.transforms.functional as F


plt.rcParams["savefig.bbox"] = 'tight'


def show(imgs):
    if not isinstance(imgs, list):
        imgs = [imgs]
    fig, axs = plt.subplots(ncols=len(imgs), squeeze=False)
    for i, img in enumerate(imgs):
        img = img.detach()
        img = F.to_pil_image(img)
        axs[0, i].imshow(np.asarray(img))
        axs[0, i].set(xticklabels=[], yticklabels=[], xticks=[], yticks=[])
    plt.show()


from torchvision.utils import make_grid
from torchvision.io import read_image
from pathlib import Path

dog1_int = read_image(str('C:\YXL\papers\Subjective_Evaluation\LOL/fourth_photo\circle/780.png'))
dog2_int = read_image(str('C:\YXL\papers\Subjective_Evaluation\LOL/fourth_photo\circle/780.png'))
dog_list = [dog1_int, dog2_int]

grid = make_grid(dog_list)
show(grid)
























