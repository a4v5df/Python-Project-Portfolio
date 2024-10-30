import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from mpl_toolkits.mplot3d import Axes3D

# f(x)
def Input_func():
    
    return

# F-series
def F_series(L,n,np_x):
    a_0, k = integrate.quad(func,-L,L)
    coef = np.array([a_0 /(2*L)])
    for i in range(1,n+1):
        a_coef, _ = integrate.quad(lambda x: func(x)*np.cos(n*np.pi*x/L),-L,L)
        b_coef, _ = integrate.quad(lambda x: func(x)*np.sin(n*np.pi*x/L),-L,L)
        coef = np.append(coef,[a_coef/L,b_coef/L])
    count = 0
    result=0
    for i in range(1,n+1,2):
        count+=1
        result += coef[i]*np.cos(count*np_x*np.pi/L)+coef[i+1]*np.sin(count*np_x*np.pi/L)
    result+=coef[0]

    return result

# Complex F-series
def Complex_F():

    return 

# F_integrate
def F_integrate():

    return 


def main():
    func = Input_func()
    F_case = input("1: F_series\n 2: Complex F_series\n 3: F_integrate\n")
    if F_case == '1':
        F_series()
    elif F_case == '2':
        Complex_F()
    elif F_case == '3':
        F_integrate()
    
    #축, 중심선, 좌표표시 등
    plt.plot(np.pi,0,'bo') # 점찍기
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axis([-2*np.pi,2*np.pi,-2*np.pi,2*np.pi]) #그래프 범위
    plt.hlines(0, x_min, x_max, color='black', linestyle='solid', linewidth=2) # x축
    plt.vlines(0, x_min, x_max, color='black', linestyle='solid', linewidth=2) # y축
    plt.legend() 
    plt.show()

while(True):
    main()
    if(input("press \'q\'")=='q'):
        break