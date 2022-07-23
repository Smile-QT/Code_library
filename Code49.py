
# 迁移学习，测试模型的加载

# 测试模型的加载
model = resnet34(num_classes=5)
# load model weights
model_weight_path = "./resNet34.pth"
model.load_state_dict(torch.load(model_weight_path, map_location=device))
model.eval()











