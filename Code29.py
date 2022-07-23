
# 在test集上评估
def show_predictions(model, class_names, n_imgs=6):
    model.eval()
    images_handled = 0
    plt.figure()

    with torch.no_grad():
        #         my_font = FontProperties(fname = 'SimHei.ttf', size =12)
        my_font = FontProperties(size=12)

        for i, (inputs, labels) in enumerate(data_loaders['test']):
            inputs = inputs.to(device)
            labels = labels.to(device)
            outputs = model(inputs)
            _, preds = torch.max(outputs, dim=1)
            for j in range(inputs.shape[0]):
                images_handled += 1
                ax = plt.subplot(2, n_imgs // 2, images_handled)
                ax.set_title(f'predicted : {class_names[preds[j]]}', fontproperties=my_font)
                imshow(inputs.cpu().data[j])
                ax.axis('off')
                if images_handled == n_imgs:
                    return


show_predictions(best_model, class_names, n_imgs=8)
