
# 迁移学习，创建模型对象
from torchvision import models  # models:用于迁移学习，导入resnet50
import torch.nn as nn
device = 'cpu'

def create_model(n_classes):
    model = models.resnet50(pretrained = True)  # 下载预训练模型
    # 全连接层输入特征
    n_features = model.fc.in_features
    # 新的全连接层输入特征
    model.fc = nn.Linear(n_features, n_classes)  # 修改全连接层，此处只是增加了一个全连接层
    return model.to(device)

# 创建模型对象
class_names = 2  # 最终你需要把数据分成几类
clf_model = create_model(class_names)


# 输出整个神经网络模型框架
print(clf_model)
