import math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

def calc_e_small(x):
    n=10
    f=np.arange(1, n+1).cumprod()
    b=np.array([x]*n).cumprod()
    return np.sum(b/f)+1

def calc_e(x):
    reverse=False
    if x<0:         # treat negative value
       x=-x
       reverse=True
    ln2=0.69314718055994530941723212145818
    c=x/ln2
    a=int(c+0.5)
    b=x-a*ln2
    y=(2**a)*calc_e_small(b)
    if reverse:
        return 1/y
    return y

if __name__=="__main__":
    t1=np.linspace(-2, 0, 10, endpoint=False)
    t2=np.linspace(0, 2, 20)
    t=np.concatenate((t1, t1))
    print t       # value of x-axis
    y=np.empty_like(t)
    for i, x in enumerate(t):
        y[i]=calc_e(x)
        print 'e^', x, '=', y[i], '(approximate value)\t', math.exp(x),
        # print 'error:', y[i]-math.exp(x)
    mpl.rcParams['font.sans-serif']=[u'SimHei']
    mpl.rcParams['axes.unicode_minus']=False
    plt.plot(t, y, 'r-', t, y, 'go', linewidth=2)
    plt.title(u'Taylor expansion application', fontsize=18)
    plt.xlabel('x', fontsize=15)
    plt.ylabel('exp(x)', fontsize=15)
    plt.grid(True)
    plt.show()
    
