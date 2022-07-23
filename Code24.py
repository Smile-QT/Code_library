
# 下载已经训练好的模型
from torchvision import models  # models:用于迁移学习，导入resnet50

model = models.resnet50(pretrained=True)  # 下载预训练模型
