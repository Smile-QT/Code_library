（1）Code01.py：
##### 使用opencv打开并处理图片，然后使用Matplotlib保存图片

（2）Code02.py: 
##### 将张量保存为图片

（3）Code03.py: 
##### 爬取一个抖音视频的评论，并将一些表情包删除了

（4）Code04.py: 
##### plt关闭坐标轴

（5）Code05.py: 
##### 把list类型和numpy类型转换成tensor类型

（6）Code06.py: 
##### 将若干张图片拼成一张图片展示
##### 展示出来的图片的宽度：nrow, 高度：len(imge)/nrow

（7）Code07.py: 
##### 读取并显示一张图片
##### 我感觉imread所有格式图片都可以读取
（8）Code08.py: 
##### 计算两个数之和
##### input 接收的所有数据都会变成字符串
##### 所以当接收完数据后，需要对数据进行处理。

（9）Code09.py: 
##### python三种输出格式

（10）Code10.py: 
##### 将给定图像随机裁剪为不同的大小和宽高比，然后缩放所裁剪得到的图像为制定的大小
##### 由于是随机裁剪，所以最后得到的figure02，figure03，figure04都是不一样的


（11）Code11.py: 
##### transforms.RandomHorizontalFlip() 以给定的概率随机水平旋转给定的PIL的图像，默认为0.5

（12）Code12.py: 
##### transforms.ToTensor() 将给定图像转为Tensor

（13）Code13.py: 
##### transforms.Normalize(） 归一化处理

（14）Code14.py: 
##### transforms.Resize(x) 将图片短边缩放至x，长宽比保持不变
##### transforms.Resize([h, w]) 而一般输入深度网络的特征图长宽是相等的，就不能采取等比例缩放的方式了，需要同时指定长宽
##### 例如transforms.Resize([224, 224])就能将输入图片转化成224×224的输入特征图


（15）Code15.py: 
##### 查看张量的维数

（16）Code16.py: 
##### 将图片数据转化成张量

（17）Code17.py: 
##### shape、size、type对于张量的作用
##### shape:查看张量的维数
##### size：查看的好像是img存在的内存位置
###### type：查看img存放的数据类型，如int、float、tensor等

（18）Code18.py: 
##### 调整张量的维度顺序

（19）Code19.py: 
##### transforms.RandomRotation(degrees=15) 随机旋转

（20）Code20.py: 
##### transforms.CenterCrop(size= 224)
##### 将给定的PIL.Image进行中心切割，得到给定的size，size可以是tuple，(target_height, target_width)。size也可以是一个Integer，在这种情况下，切出来的图片的形状是正方形

（21）Code21.py: 
##### transforms.Resize(size=256)
##### 改变图片的像素大小

（22）Code22.py: 
##### 可视化显示数据增强后的图片（注意:中文字符显示）

（23）Code23.py: 
##### 张量转化成数组
##### 数组转化成张量
###### 列表转化成张量
##### 列表转化成数组


（24）Code24.py: 
##### 下载已经训练好的模型

（25）Code25.py: 
##### 迁移学习，创建模型对象

（26）Code26.py: 
##### 深度学习模型 函数：训练

（27）Code27.py: 
##### 深度学习模型函数：验证

（28）Code28.py: 
##### 函数：开始训练

（29）Code29.py: 
##### 在test集上评估

（30）Code30.py: 
#####  混淆矩阵

（31）Code31.py: 
##### enumerate对于字典的使用，i是字典的值，w是字典的键

（32）Code32.py: 
##### 把一个列表转置

（33）Code33.py: 
##### PyTorch的 transpose、permute、view、reshape的区别

（34）Code34.py: 
##### 查看张量的维度

（35）Code35.py: 
##### 计算张量中元素的个数

（36）Code36.py: 
##### range torch.range torch.arange区别

（37）Code37.py: 
##### range torch.range torch.arange区别
##### torch.range torch.arange最后的结果的张量

（38）Code38.py: 
##### expand
##### 返回tensor的一个新视图，单个维度扩大为更大的尺寸。
##### tensor也可以扩大为更高维，新增加的维度将附在前面。 扩大tensor不需要分配新内存，
##### 只是仅仅新建一个tensor的视图，其中通过将stride设为0，一维将会扩展位更高维。
##### 任何一个一维的在不分配新内存情况下可扩展为任意的数值。
##### 使用expand()函数的时候，x自身不会改变，因此需要将结果重新赋值。

（39）Code39.py: 
##### 用numpy创建一维数组
##### dtype：查看数据结构中保存到的数据类型
##### type：查看数据结构类型

（40）Code40.py: 
##### 创建全是1的张量
##### 方法：torch.tensor.ones(维度结构)

（41）Code41.py: 
##### enumerate
##### enumerate()是python的内置函数
##### enumerate在字典上是枚举、列举的意思
##### 对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值
##### enumerate多用于在for循环中得到计数
##### 当enumerate的参数是字典时，enumerate提取的是字典的键，不会提取字典的值

（42）Code42.py: 
##### append、extend、expand()函数详解
##### a.append(b)：是将b原封不动的追加到a的末尾上，会改变a的值，其中，b可为列表、元组、字符串、一串数 / 字符 / 字符串
##### a.extend(b)：是将b拆开后追加到a的末尾上，会改变a的值，其中，b可为列表、元组、字符串、一串数/字符/字符串

（43）Code43.py: 
##### unsqueeze()函数、squeeze()函数介绍

（44）Code44.py: 
##### 将numpy.ndarray变成一个张量
##### torch.from_numpy(ndarray) → Tensor，
##### 即 从numpy.ndarray创建一个张量。

（45）Code45.py: 
##### pytorch masked_fill方法简单理解
##### masked_fill方法有两个参数，maske和value，mask是一个pytorch张量（Tensor），
##### 元素是布尔值，value是要填充的值，填充规则是mask中取值为True位置对应于self的相应位置用value填充。
##### masked_fill_(mask, value)
##### 用value填充tensor中与mask中值为1位置相对应的元素。mask的形状必须与要填充的tensor形状一致。
##### masked_fill_(mask == 0, value)
##### 用value填充tensor中与mask中值为0位置相对应的元素。mask的形状必须与要填充的tensor形状一致。

（46）Code46.py: 
##### tf.nn.functional.softmax(x,dim = -1)   一般会有设置成dim=0,1,2,-1的情况
##### 中的参数dim是指维度的意思，
##### 设置这个参数时会遇到0,1，2，-1等情况，特别是对2和-1不熟悉，
##### 细究了一下这个问题,查了一下API手册，是指最后一行的意思。

（47）Code47.py: 
##### 显示一张图片

（48）Code48.py: 
##### 1.访问列表中的值
##### 2.修改列表中的值
##### 3.删除列表元素

（49）Code49.py: 
##### 获取计算机GPU或者CPU

（50）Code50.py: 
##### 迁移学习，测试模型的加载

（51）Code51.py: 
##### repeat()


（52）Code52.py: 
##### 遍历网络模型中的权重，查看是否冻结
##### requires_grad=False :冻结权重
##### requires_grad=Ture：不冻结权重

（53）Code53.py: 
##### 计算两张图片之间的PSNR和SSIM值

（54）Code54.py: 
##### Tensor 和 NumPy 变量互相转化
##### tuple 和 list 变量相互转化

（55）Code55.py: 
##### 使用opencv读取彩色图片，并将图片转化成RGB格式

（56）Code56.py: 
##### 读取RGB图片，并将图片转化成灰度图片

（57）Code57.py: 
##### 计算两张图片之间的L1loss

（58）Code58.py: 
##### 对图像做快速傅里叶变换

（59）Code59.py: 
##### 对图像做快速傅里叶变换之后，计算两个图像在频域之间的L1loss损失(由于计算L1loss的两个图片的尺寸需要一样大，所以示例中使用的是同一张图片)

（60）Code60.py: 
##### 垂直镜像翻转图像

（61）Code61.py: 
##### 将图片逆时针旋转60度，并缩小为0.5倍

（62）Code62.py: 
##### X轴向左边平移图像大小的1/5，Y轴向下平移图像大小的的1/4

（63）Code63.py: 
##### 用基于阈值的方法实现图像边缘轮廓提取

（64）Code64.py: 
##### 查询python中一个变量的类型type（变量名）

（65）Code65.py: 
##### 设置画布大小

（66）Code66.py:
##### 在pytorch中实现将sobel算子和卷积层结合来提取图像中物体的边缘轮廓图

（67）Code67.py:
##### 给加入椒盐噪声、高斯噪声的图像进行均值滤波。

（68）Code68.py:
##### 给加入均匀噪声的图像中值滤波

（69）Code69.py:
##### 实现基于SVM算法的图像分割。

（70）Code70.py:
##### 实现基于KMEANS的图像分割。

（71）Code71.py:
##### Python遍历文件夹下所有文件，并返回文件绝对地址列表

（72）Code72.py:
##### 在指定位置创建一个指定的文件（不是文件夹）

（73）Code73.py:
##### 在指定位置创建一个指定的文件夹（不是文件）

（74）Code74.py:
##### 根据提供的抖音网址，下载抖音视频

（75）Code75.py:
##### 地址连接

（76）Code76.py:
##### 获取excel中指定列的所有数据
##### 获取第0列的数据：抖音视频的网址的序号，序号是从1开始的。
##### 读取原始excel表中的抖音视频的路径到指定的列表中

（77）Code77.py:
##### 使用python在已存在的excel数据表中的特定位置写入数据
##### excel表中的行和列都是从1开始的

（78）Code78.py:
##### 批量爬取抖音评论
##### chrome驱动程序选择网址：https://blog.csdn.net/python_TB/article/details/124303116


（79）Code79.py:
##### 爬取一个抖音视频的点赞数、评论数、收藏数

（80）Code80.py:
##### 批量爬取抖音视频的点赞数、评论数、收藏数

（81）Code81.py:
##### 批量爬取抖音视频的文案

（82）Code82.py:


（83）Code83.py:




