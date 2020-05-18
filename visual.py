import numpy as np
import matplotlib.pyplot as plt

v = np.loadtxt('datav')
rv = np.loadtxt('datarv')
N = 100000
en = 100
x = np.arange(N)
sample = np.arange(1000, N, step=1000,dtype=int)

plt.cla()
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
# for j in range(en):
#     ax1.scatter(x[sample], v[j,sample], color='black', s=0.05)
# for j in range(en):
#     ax2.scatter(x[sample], rv[j,sample], color='black', s=0.05)
ax1.plot(x[1000:],np.mean(v,axis=0)[1000:])
ax2.plot(x[1000:],np.mean(rv,axis=0)[1000:])

plt.savefig("avg.jpg")