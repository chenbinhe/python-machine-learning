'''
This code compares the speed of calculating Z between vector and for
Sigmoid(z) used in Logistic Regression
'''
import numpy as np
import time

a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()
c = np.dot(a,b)
toc = time.time()
print("the vectorized version :" + str(1000*(toc-tic)) + "ms")
print(c)

c= 0
tic = time.time()
for i in range(1000000):
    c += a[i] * b[i]
toc = time.time()
print("For loop :" + str(1000*(toc - tic)) + "ms")
print(c)