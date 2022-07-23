
# 函数：开始训练
def train_model(model, data_loader, dataset_size, device, n_epochs = 1):
    # 优化器
    optimizer = torch.optim.Adam(model.parameters(), lr = 0.001)
    # 动态学习率
    scheduler = lr_scheduler.StepLR(optimizer, step_size = 7, gamma  = 0.1)
    # 损失函数
    criterion = nn.CrossEntropyLoss().to(device)
    # 假设最好的accuracy，history
    best_accuracy = 0.0
    history = defaultdict(list)  # 构建一个默认value为list的字典

    for epoch in range(n_epochs):
        print(f'Epoch : {epoch + 1} / {n_epochs}')
        print('_' * 20)
        train_loss, train_accuracy = train(model, data_loader['train'], criterion, optimizer, device, scheduler, dataset_size['train'])
        print(f'Train Loss : {train_loss},Train accuracy : {train_accuracy}' )
        val_loss, val_accuracy = evaluation(model, data_loader['val'], criterion, device, dataset_size['val'])
        print(f'val loss ： {val_loss}, val accuracy : (val_accuracy')

        # 保存所有结果
        history['train_acc'].append(train_accuracy)
        history['train_loss'].append (train_loss)
        history['val_acc'].append(val_accuracy)
        history['val_loss'].append(val_loss)

        if val_accuracy > best_accuracy:
            # 保存最佳模型
            torch.save(model.state_dict(), 'best_model_state_2.pkl')
            # 最好得分
            best_accuracy = val_accuracy
    print(f'Best Accuracy : {best_accuracy}')

    # 加载模型
    model.load_state_dict(torch.load('best_model_state_2.pkl'))

    return model, history

# %%time
best_model, history = train_model(clf_model, data_loaders, dataset_size, device)
