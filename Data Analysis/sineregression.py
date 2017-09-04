import numpy as np
from scipy.optimize import leastsq
import pylab as plt
def sinR():
    f=open("12_31_15.csv",'r')
    lineNum=1
    timeA=[]
    voltageSet=[]
    for line in f:
        if lineNum==1:
            #station=line.split(",")[0]
            #statName=line.split(",")[1]
            lineNum+=1
        elif lineNum==2:
            #time=line.split(",")[0]
            #voltage=line.split(",")[1]
            timeA.append(line.split(",")[0])
            voltageSet.append(line.split(",")[1])
    N = 100 # number of data points
    t = np.linspace(0, 4*np.pi, N)
    data = [1,2,3,4,5,6,7,8,9]
    #3.0*np.sin(t+0.001) + 0.5 + np.random.randn(N)
    guess_mean = np.mean(data)
    guess_std = 3*np.std(data)/(2**0.5)
    guess_phase = 0
    print data

# we'll use this to plot our first estimate. This might already be good enough for you
    data_first_guess = guess_std*np.sin(t+guess_phase) + guess_mean

# Define the function to optimize, in this case, we want to minimize the difference
# between the actual data and our "guessed" parameters
    optimize_func = lambda x: x[0]*np.sin(t+x[1]) + x[2] - data
    est_std, est_phase, est_mean = leastsq(optimize_func, [guess_std, guess_phase, guess_mean])[0]

# recreate the fitted curve using the optimized parameters
    data_fit = est_std*np.sin(t+est_phase) + est_mean

    plt.plot(data, '.')
    plt.plot(data_fit, label='after fitting')
    plt.plot(data_first_guess, label='first guess')
    plt.legend()
    plt.show()
