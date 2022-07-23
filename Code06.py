
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




