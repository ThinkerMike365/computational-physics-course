import numpy as np
import matplotlib.pyplot as plt
from numba import jit,int8,float32
J = 1                                                #初始化参数
kT = 1
ising = np.zeros((7,7))
def init():                                          #初始化模型
    for i in range(1,6):
        for j in range(1,6):
            np.random.seed()
            a = np.random.random_sample()
            if a>=0.5:
                ising[i][j]=1
            else:
                ising[i][j]=-1
init()
@jit(float32(int8,int8,int8[::]))
def H(i,j,A=ising):                                  #定义能量
    e_ij = -J/2*(A[i][j]*(A[i-1][j]+A[i+1][j]+A[i][j-1]+A[i][j+1]))
    return e_ij
@jit(float32(int8,int8,int8[::]))
def P(i,j,A=ising):                                  #计算翻转概率
    delta_h = -4*H(i,j)
    p = np.exp(-delta_h/kT)
    return p
@jit(float32(int8[::]))
def calc_energy(A=ising):                            #计算模型能量
    e = 0
    for i in range(1,6):
        e_i = 0
        for j in range(1,6):
            e_ij = H(i,j)
            e_i = e_i + e_ij
        e = e + e_i
    return e
energy_list = np.array([])                           #蒙特卡洛模拟
for _ in range(100000):
    if _%100 == 0:
        print(_)
        np.random.seed()
    i = np.random.randint(1,5)
    j = np.random.randint(1,5)
    ran = np.random.random_sample()
    p = P(i,j)
    if ran < p:
        ising[i][j] = -ising[i][j]
    else:
        pass
    e = calc_energy()
    energy_list = np.append(energy_list,e)
energy = np.average(energy_list)                    #计算能量平均值
print(energy)