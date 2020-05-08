import numpy as np
import matplotlib.pyplot as plt
import time

for j in range(100):
    m = 50
    q = 2.0
    state = np.zeros(m)

    N = 100000
    v = np.zeros(N)
    est = np.zeros(N)
    hll = np.zeros(N)
    x = np.arange(N)
    fm = 0 # running first moment
    sm = 0 # running second moment
    area = 1 # remaining area

    for t in range(N):
        c = np.random.randint(0,m)
        k = np.random.geometric(1/q)
        if k > state[c]:
            fm += 1/area
            sm += 1/area/area
            area += (np.power(1/q,k)-np.power(1/q,state[c]))/m
            state[c] = k
        v[t] = np.sqrt(sm/fm/fm)
        hll[t] = 1/np.sum(np.power(1/q,state)) * m * m * 0.7
        est[t] = fm


    plt.cla()
    f, (ax1, ax2) = plt.subplots(1, 2)
    hll = hll*N/hll[N-1]
    est = est*N/est[N-1]
    ax1.plot(x[1000:], v[1000:])
    ax2.plot(x[1000:], hll[1000:], color='red')
    ax2.plot(x[1000:], est[1000:], color='blue')
    ax2.plot(x[1000:], x[1000:], color='black')

    plt.savefig("figures/experiment"+str(j)+".jpg")