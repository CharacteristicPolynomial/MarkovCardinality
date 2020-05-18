import numpy as np
import matplotlib.pyplot as plt
import time

en = 100

N = 100000
x = np.arange(N)
v = np.zeros([en,N])
rv = np.zeros([en,N])
for j in range(en):
    print(j)
    m = 64
    q = 2.0
    state = np.zeros(m)

    est = np.zeros(N)
    hll = np.zeros(N)
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
        v[j,t] = sm/fm/fm
        rv[j,t] = (fm/(t+1)-1)*(fm/(t+1)-1)
        hll[t] = 1/np.sum(np.power(1/q,state)) * m * m * 0.709
        est[t] = fm


    # plt.cla()
    # f, (ax1, ax2) = plt.subplots(1, 2)
    # ax1.plot(x[1000:], v[j,1000:])
    # ax1.plot(x[1000:], rv[j,1000:])
    # ax2.plot(x[1000:], hll[1000:], color='red')
    # ax2.plot(x[1000:], est[1000:], color='blue')
    # ax2.plot(x[1000:], x[1000:], color='black')

    # plt.savefig("figures/experiment"+str(j)+".jpg")

np.savetxt('datav', v)
np.savetxt('datarv', rv)