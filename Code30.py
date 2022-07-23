
#  混淆矩阵
cm = confusion_matrix(y_test, y_pred)  # 计算TP, FP, TN, FN
df_cm = pd.DataFrame(cm, index = class_names, columns = class_names)
hmap = sns.heatmap(df_cm, annot = True)
hmap.yaxis.set_ticklabels(hmap.yaxis.get_ticklabels(), rotation = 0, ha = 'right' )
hmap.xaxis.set_ticklabels(hmap.xaxis.get_ticklabels(), rotation = 0, ha = 'right' )
plt.ytable('True Label')
plt.ytabel('Pred Label')
plt.show()
