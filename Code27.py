
# 函数：验证
def evaluation(model, data_loader, criterion, device, n_examples):
    model.eval()
    eval_loss = []
    correct_pred = 0
    with torch.no_grad():
        for inputs, labels in data_loader:
            inputs = inputs.to(device)
            labels = labels.to(device)
            outputs = model(inputs)  # 输出
            loss = criterion(outputs,labels)  # 损失
            _, preds = torch.max(outputs, dim= 1)  # 互获取到概率最大值的索引
            correct_pred += torch.sum(preds == labels)  # 累计正确率
            eval_loss.append(loss.item())  # 累计损失
    return np.mean(eval_loss), correct_pred.double() / n_examples
