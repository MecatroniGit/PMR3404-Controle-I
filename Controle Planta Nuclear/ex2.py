# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 09:32:10 2020

@author: eduardo
"""
import numpy as np
import cmath as cm
import control as co_general
import matplotlib.pyplot as plt
from control.matlab import *
from scipy import interpolate
from grafico_margens import plot_margins
plt.close('all')

T = 0.4
tau = 0.2

s = tf([1,0],1)
num, den = pade(T,7)
Gdelay = tf(num,den)
G = 1/(tau*s+1) * Gdelay

Mp = 0.2
zeta = abs(np.log(Mp)/np.sqrt(np.power(np.pi, 2)+np.power(np.log(Mp), 2)))
MF = np.arctan(2*zeta/(np.sqrt(-2*zeta**2+np.sqrt(1+4*zeta**2))))*180/np.pi
print(MF)
print(zeta)

"""
Gc = K2*(1+K1*s/K2)/s

K1/K2 = tau para cancelamento do polo da planta
"""
K2 = 1

Gc = K2*(1+tau*s)/s

plot_margins(G*Gc)

#MG = -180+MF+8
MG = 11.8 - 8
K2 = 10**(MG/20)
print(K2)

Gc = K2*(1+tau*s)/s

plt.figure()
y , t = step(feedback(G*Gc))
plt.plot(t,y)





