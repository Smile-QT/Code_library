
# 函数：训练
def train(model, data_loader, criterion, optimizer, device, scheduler, n_examples):
    model.train()
    train_loss = []
    correct_pred = 0
    for inputs, labels in data_loader:
        inputs = inputs.to(device)
        labels = labels.to(device)
        optimizer.zero_grad()  # 梯度置零
        outputs = model(inputs)  # 输出
        loss = criterion(outputs, labels)  # 计算损失
        _, preds = torch.max(outputs, dim = 1)  # 获取到概率最大值的索引
        correct_pred += torch.sum(preds == labels)  # 累计正确数
        train_loss.append(loss.item())  # 累计损失
        loss.backward()  # 反向传播
        optimizer.step()  # 更新参数
    scheduler.step()  # 更新学习率
    # 返回平均损失， 平均准确率
    return np.mean(train_loss), correct_pred.double()/n_examples
