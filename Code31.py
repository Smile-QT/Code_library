
# enumerate对于字典的使用，i是字典的值，w是字典的键
tgt_vocab = {'P' : 0, 'i' : 1, 'want' : 2, 'a' : 3, 'beer' : 4, 'coke' : 5, 'S' : 6, 'E' : 7, '.' :8}
idx2word = {i: w for i, w in enumerate(tgt_vocab)}
print(idx2word)

