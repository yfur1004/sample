''' This code is very easy '''
import numpy as np
import sys

a = np.array([1, 2, 3])
b = np.array([0, 1, 2])
c = np.dot(a, b)
print(c)

for i in range(10):
    print(i)

while i < 100:
    i = i + 1
    print(i**2)

'''fibo'''
i = 1
j = 1
print(j)
print(i)

while i < 100:
    k = j
    j = i
    i = j + k
    print(i)

x = 2
y = 3
print(y**2)

print(sys.version)
