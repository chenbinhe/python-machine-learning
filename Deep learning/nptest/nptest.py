import numpy as np
a = np.zeros(10, dtype=int)
print(a)

b = np.zeros((4,5), dtype=float)
print(b)

c = np.sum([0.5,0.7,0.2,1.5], dtype=np.int32)
print(c)

c = np.sum([0.5,0.7,0.2,1.5])
print(c)


d = np.array([[56.0,0.0,4.4,68.0],
              [1.2,104.0,52.0,8.0],
              [1.8,135.0,99.0,0.9]])
print(d)
cal = d.sum(axis=0)#希望矩阵在竖向求和,axis=1则可以水平求和
print(cal)
cel = d.sum(axis=1)
print(cel)

percentage = 100*d/cal.reshape(1,4) #reshape o(1) 将cal变成1行4列
print(percentage)


e = np.random.rand(5)
print(e)
print(e.shape)#在神经网络编程，不要用这个(5,)秩为1的数组
e = np.random.rand(5,1)#用这样定义死一个数组的行列
print(e)
assert(e.shape == (5,1))#用这个assert可以保证e是一个5行1列的矩阵，且其运算量不大