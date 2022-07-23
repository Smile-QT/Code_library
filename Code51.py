
# 遍历网络模型中的权重，查看是否冻结
# requires_grad=False :冻结权重
# requires_grad=Ture：不冻结权重
for i,p in enumerate(model.parameters()):
        print(p.requires_grad)
