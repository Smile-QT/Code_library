
# 获取计算机GPU或者CPU
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')  # 选择使用GPU运行程序还是CPU运行程序
#  创建一个模型，并把这个模型放在设备上面去
model = Digit().to(DEVICE)
