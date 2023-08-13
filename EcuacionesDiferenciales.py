#Ecucaion diferencial
#AUTOR: KEYTEL PUMAYLLE RAMIREZ
# Ejercicios de Reactores
from tokenize import PlainToken
from scipy.integrate import solve_ivp
import  matplotlib.pyplot as plt
import numpy as np

def sistemaReacciones(V,y):
    y1 = y[0] #Residuos
    y2 = y[1] #vgo
    y3 = y[2] #Destilables
    y4 = y[3] #naftas
    y5 = y[4] #gases

    dyResiduos = (-k1*y1-k2*y1-k3*y1-k4*y1)/v0
    dyVGO = (k1*y1-k5*y2-k6*y2-k7*y2)/v0
    dyDestilables = (k2*y1+k5*y2-k8*y3-k9*y3)/v0
    dyNaftas = (k3*y1+k6*y2+k8*y3-k10*y4)/v0
    dyGases = (k4*y1+k7*y2+k9*y3+k10*y4)/v0

    return np.array([dyResiduos, dyVGO, dyDestilables, dyNaftas, dyGases])



barriles_dia= 21000
#flujo volumetrico
v0 = barriles_dia * 0.006624470622 #m3/h
densidad_crudo = 0.715 #g/cm3

flujo_masico_0 = v0 * densidad_crudo * 100**3 #g/h
D = 3.5 #m

#Orden de los Crudos
#     res,   vgo,   des,   naf   gas
y0 = [0.394, 0.281, 0.204, 0.121, 0]

k1 = 0.147
k2 = 0.022
k3 = 0.020
k4 = 0.098
k5 = 0.057
k6 = 0.007
k7 = 0
k8 = 0.003
k9 = 0
k10 = 0

#intervalo de Integracion
V_inicial = 0
V_final = 0
sol = solve_ivp(sistemaReacciones, (V_inicial, V_final), y0)
sol