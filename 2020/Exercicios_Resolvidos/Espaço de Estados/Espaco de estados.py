# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:22:59 2020

@author: dueiras
"""

import numpy as np
import cmath as cm
import control as co_general
import matplotlib.pyplot as plt
from control.matlab import *

A = [[0.5,1],
     [1, 0]]

B = [[1],
     [0]]

C = [0, 1]

D = 0

sys = ss(A,B,C,D)

#simulacao com condicoes iniciais nao nulas
X0 = [0.1,0]
n=1000
T = np.linspace(0,20,n)
yout,t,xout = initial(sys,T,X0,return_x=True)
plt.figure()
plt.plot(t,yout)
plt.title('Saída inicial do sistema')
plt.xlabel('Time (sec)')
plt.ylabel('Saída')

#Controlabilidade
CT = ctrb(A,B)
print("A controlabilidade do sistema é:", np.linalg.matrix_rank(CT))
"Como rank(CT) é igual ao número de estados, o sistema é controlável"

pk = [-0.3,-0.7] #Polos do requisito
K = place(A,B,pk) #Matriz com os polos desejados
kr = 1
sys_mf = ss(A-B*K , kr*B , C-D*K , kr*D) #Sistema compensado 

#Verificar saída do sistema

yout, y = step(sys_mf, T)
plt.figure()
plt.plot(t,yout)
plt.title('Controle inicial kr=1')
plt.xlabel('Time (sec)')
plt.ylabel('Saída')

"Sistema ainda não atingiu erro nulo em regime"

#Utilizar outro kr

Kr = 1/dcgain(sys_mf)
print("kr = ", Kr)
sys_mf = ss(A-B*K,Kr*np.asarray(B),C,D)
print("Novo sistema:")
print(sys_mf)

yout, y = step(sys_mf, T)
plt.figure()
plt.plot(t,yout)
plt.title('Controle com novo kr')
plt.xlabel('Time (sec)')
plt.ylabel('Saída')

yout,t,xout = initial(sys_mf,T,X0,return_x=True)
plt.figure()
plt.plot(t,yout)
plt.title('Saída com condição não nula do sys compensado')
plt.xlabel('Time (sec)')
plt.ylabel('Saída')

# =============================================================================
# R = np.zeros((n,1))
# R[0:n,0] = 0.001
# 
# yout,t,xout = lsim(sys_mf,R,T)
# plt.figure()
# plt.plot(t,yout)
# plt.title('Saída com novo kr')
# plt.xlabel('Time (sec)')
# plt.ylabel('Ball Position (m)')
# =============================================================================


# =============================================================================
# #polos escolhidos 1
# pole = [-50,-10+10j,-10-10j]
# K = place(A,B,pole)
# sys_cl = ss(A-B*K , B , C , 0)
# 
# X0 = [0.01,0,0]
# T = np.linspace(0,2,1000)
# yout,t,xout = initial(sys_cl,T,X0,return_x=True)
# plt.figure()
# plt.plot(t,yout)
# plt.title('Closed-Loop Response to Non-Zero Initial Condition')
# plt.xlabel('Time (sec)')
# plt.ylabel('Ball Position (m)')
# 
# #polos escolhidos 2
# pole = [-100,-20+20j,-20-20j]
# K = place(A,B,pole)
# sys_cl = ss(A-B*K,B,C,0)
# 
# X0 = [0.01,0,0]
# T = np.linspace(0,2,1000)
# yout,t,xout = initial(sys_cl,T,X0,return_x=True)
# plt.figure()
# plt.plot(t,yout)
# plt.title('Closed-Loop Response to Non-Zero Initial Condition')
# plt.xlabel('Time (sec)')
# plt.ylabel('Ball Position (m)')
# 
# 
# #polos escolhidos 2 e referência
# pole = [-100,-20+20j,-20-20j]
# K = place(A,B,pole)
# sys_cl = ss(A-B*K,B,C,0)
# 
# Kr = 1/dcgain(sys_cl)
# sys_cl = ss(A-B*K,Kr*np.asarray(B),C,0)
# 
# n=1000
# T = np.linspace(0,2,n)
# R = np.zeros((n,1))
# R[0:n,0] = 0.001
# 
# yout,t,xout = lsim(sys_cl,R,T)
# plt.figure()
# plt.plot(t,yout)
# plt.title('Closed-Loop Response to Non-Zero Initial Condition')
# plt.xlabel('Time (sec)')
# plt.ylabel('Ball Position (m)')
# 
# u = K * xout.T +  (R*Kr).T
# plt.figure()
# plt.plot(t,u.T)
# plt.title('Closed-Loop Response to Non-Zero Initial Condition')
# plt.xlabel('Time (sec)')
# plt.ylabel('Input (V)')
# 
# 
# #LQR
# R = 1
# Q = [[1,0,0],
#     [0,1,0],
#     [0,0,1]]
# K , S , E = lqr(A,B,Q,R)
# 
# u = K * xout.T +  (R*Kr).T
# 
# plt.figure()
# plt.plot(t,u.T)
# plt.title('Closed-Loop Response to Non-Zero Initial Condition')
# plt.xlabel('Time (sec)')
# plt.ylabel('Input (V)')
# =============================================================================
