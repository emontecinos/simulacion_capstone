import random
import matplotlib.pyplot as plt


a = []
b = []
for i in range(10):
    b.append(i)
for i in range(10):
    a.append(random.expovariate(0.3))
plt.plot(b,a)
