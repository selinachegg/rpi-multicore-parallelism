import random
import numpy as np

p = -12

f = [random.uniform(1.2, 2.4) for i in range(20)]
n = [1,2,3,4,5,6,7,8]
C = []
idx0 = []
idx1 = []
for i in range(8):
    for j in range(20):
        C.append(-12.64 + 15.96 * f[j] + 3.66 * n[i])
        idx0.append(i)
        idx1.append(j)
element = min(C)
index = np.argmin(C)

print("nombre de coeurs")
print(n[idx0[index]])
print("frequence")
print(f[idx0[index]])

