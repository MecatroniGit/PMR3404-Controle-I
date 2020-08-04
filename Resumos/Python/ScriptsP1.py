# -*- coding: utf-8 -*-
"""
Created on Wed May 20 14:40:06 2020

@author: dueir
"""


import numpy as np
import control as co_general
import matplotlib.pyplot as plt
import control.matlab as co
from control.matlab import step as step
from control.matlab import tf as tf

"""
LUGAR DAS RAIZES
"""
s = tf('s')
K = 1
num = ((1)*(1))
den = ((s-2)*(s+1)*(s+5))
#den = (1*(s*s-1)*(0*s+1))
#den = (s*(s+4))
G = K*num/den
print(G)
#co.rlocus(G)

z = np.complex(-8, 10.7)
K = 1/np.abs((1+0.071*z)*2.9/(z*(0.3*z+1)))
#print(K)

def sobressinal():
    x = np.linspace(0,10,100)
    y = np.exp(-np.pi*x/np.sqrt(1-x**2)) 
    plt.plot(x,y) 
    plt.show() 
#sobressinal()
Mp = 0.05
zeta = -np.log(Mp)/np.sqrt(np.log(Mp)**2+np.pi**2)
print("Zeta=", zeta)

# =============================================================================
# #BAGO QUE CALCULA CONDICAO DE FASE
# def calcula_fase():
#     polo_desejado = np.complex(6.67, 6.67)
#     reald = np.real(polo_desejado)
#     imagd = np.imag(polo_desejado)
#     s = tf('s')
#     planta = (0.1*s+.22)/(0.12*s*s*s + 0.6*s*s)
#     zeros = co.zero(planta)
#     print(zeros)
#     polos = co.pole(planta)
#     print(polos)
#     ang_zeros = 0
#     for z in zeros:
#         realz = np.real(z)
#         imagz = np.imag(z)
#         ang = np.arctan(np.abs(imagd-imagz)/np.abs(reald-realz))*180/np.pi
#         if realz>reald:
#             ang = 180 - ang
#         ang_zeros += ang
#     print(ang_zeros)
#     
#     ang_polos = 0
#     for p in polos:
#         realz = np.real(z)
#         imagz = np.imag(z)
#         ang = np.arctan(np.abs(imagd-imagz)/np.abs(reald-realz))*180/np.pi
#         if realz>reald:
#             ang = 180 - ang
#         ang_polos += ang
#     print(ang_polos)
#     
#     angulo = 180 - ang_zeros + ang_polos
#     print('Angulo desejado: ', angulo)   
#     return
# #calcula_fase()
#     
# def metodo_ogata():
#     polo_desejado = np.complex(-2, 3.464)
#     real_desejado = np.real(polo_desejado)
#     img_desejado = np.imag(polo_desejado)
#     angulo_avanco = 25
#     angulo_polo_desejado = np.angle(polo_desejado)*180/np.pi
#     ang = (angulo_polo_desejado/2-angulo_avanco/2)
#     tgt = np.tan(ang*np.pi/180)
#     polo = img_desejado/tgt - real_desejado
#     
#     ang = (angulo_polo_desejado/2+angulo_avanco/2)
#     tgt = np.tan(ang*np.pi/180)
#     zero = real_desejado - img_desejado/tgt  
#     print("Polo=", -polo, "Zero=", zero)
#     return polo, zero
# #p, z = metodo_ogata()
# =============================================================================

def modulo(s):
    #G = (85*s + 510)/(s*(3610*s*s + 64180*s + 127450))
    G = 1/((s-1)*(s+1))
    Gc = (1 + 0.667*s) #(s+1.272)/((s+6.289))
    print("MODULO K=", 1/np.abs(G*Gc))
    return (1/np.abs(G*Gc))

modulo(np.complex(-1, 1))


def polos(G):
    return co.pole(G)

def zero(G):
    return co.zero(G)

def degrau(G):
    y1,t1 = co.step(co.feedback(G,1))
    plt.figure()
    plt.plot(t1,y1)
    plt.title("Step")
    plt.xlabel("Tempo[s]")
    plt.ylabel("Amplitude")
    plt.grid()
    print( co.stepinfo(co.feedback(G,1)))
s = tf('s')
G=1/(((s/0.6)+1)*(s+1))
Kp = 4
KI = 0
Kd = 4
Gc = (Kp + (KI/s) + Kd*s)
#degrau(Gc*G)

s = tf('s')
G=1/((s-1)*(s+1))
Kp = 3
Kd = 1
Gc = (Kp + Kd*s)
degrau(Gc*G)
#co.rlocus(G)


#print(co.stepinfo(co.feedback((25*40*(s+1.272))/(s*(60*s+20)*(s+6.289)), 1))['SteadyStateValue'])

G = 16/(s*(s+4))
K=5
b=5
T=10
Gc=K*(1+s*T)/(1+s*b*T)
# =============================================================================
# print(G*Gc)
# print(co.pole(G*Gc))
# print(co.pole(co.feedback(G*Gc, 1)))
# =============================================================================

