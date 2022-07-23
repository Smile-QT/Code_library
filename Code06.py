
# 将若干张图片拼成一张图片展示
# 这里的imags存放着一批图片，这里为了方便起见，就设置成列表。
# 展示出来的图片的宽度：nrow, 高度：len(imge)/nrow
import torchvision
import torch
imgs = list()
imgs = ['F:/Graduate students grade three/postgraduate studies/first year of postgraduate study/申报研究生创新项目/图片/01.jpg', 'F:/Graduate students grade three/postgraduate studies/first year of postgraduate study/申报研究生创新项目/图片/02.jpg']
imgs = torch.as_tensor(imgs)
grid_imgs = torchvision.utils.make_grid(imgs, nrow = 1)
import matplotlib as plt

plt.show(grid_imgs)





