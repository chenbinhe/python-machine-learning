# np.array  np.random.rand
    - a = np.array([1,2,3,4])
    - a = random.rand(1000000)
    - 这两个的区别是，array里必须写明[]，下面则只用给出长度，随机生成
    
# np.zeros()
    - 创建数值都是0的数组，里面记录长度,(4,5)表示4行5列,一共4个数组，每个数组5个元素，嵌套数组
    - np.zeros(10, dtype=int)
    - np.zeros((4,5), dtype=float)
    
# np.exp()  np.log()
    - 计算e指数
    - 计算log
    
# np.arange()
    - np.arange(0,20,2)
        创建一个线性数组，从0开始，到20结束，步长为2
        [0,2,4,6,8,10,12,14,16,18]
    - python与其他语言一样，一般左包含，右不包含
    
    
# np.random.rand() np.random.randn() np.random.randint()
    - rand    0,1分布
    - randn   正态分布 (0,1,(3,3)) 均值为0，标准差为1的3*3正太分布数组
    - np.random.randint(0,10,(3,3)) 0~10之间的3*3矩阵
# np.maximum()
    - 计算所有元素的最大值
    
# np.sum(a,axis= , dtype= , out= ,keepdims=)
    - a 是要进行加法运算的向量/数组/矩阵
    - axis  =0 竖向求和，=1水平求和 
    - dtype 数据以什么类型参与到求和
    - out  输出的向量/数组/矩阵，要与定义拟合
    
# np.dot()
    - 返回两个矩阵的乘积
    
 