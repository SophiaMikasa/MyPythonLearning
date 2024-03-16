import numpy as np
import random


t1 = np.array([1, 2, 3])
print(t1)
print(type(t1))

t2 = np.array(range(10))
print(type(t2))
print(t2)

t3 = np.arange(4, 10, 2)
print(t3)
print(type(t3))

print(t3.dtype)

t4 = np.array(range(1, 4), dtype="i8")
print(t4)
print(t4.dtype)

t5 = np.array([1,1,0,1,0,0],dtype=bool)
print(t5)
print(t5.dtype)

# 调整数据类型
t6 = t5.astype("int8")
print(t6)
print(t6.dtype)

t7 = np.array([random.random() for _ in range(10)])
print(t7)
print(type(t7))

t8 = np.round(t7, 2)
print(t8)
print(type(t8))

t9 = np.arange(12)
print(t9.shape)

t10 = np.array([[1, 2, 3],
                [4, 5, 6]])
print(t10.shape)

t11 = np.arange(12)
t11.reshape(3, 4)

t12 = np.arange(24).reshape((2,3,4))
print(t12)

t13 = t12.flatten()
print(t13)

print(t13+2)
print(t13/2)
print(t13*2)

t14 = np.arange(0, 24).reshape((4, 6))
t15 = np.arange(100, 124).reshape((4, 6))
print(t14 + t15)
print(t14*t15)

t16 = np.arange(0, 6)
print(t15-t16)

t17 = np.arange(4).reshape((4,1))
print(t14)
print(t14 - t17)
print(t14 * t17)

t18 = np.arange(10)
