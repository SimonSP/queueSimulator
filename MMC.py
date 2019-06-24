#!/usr/bin/env python
# -*- coding: utf-8 -*-

#PYTHON 2.7
#TEORÍA DE COLAS M/M/1 por Simón Salvo Pino

from math import exp
from math import factorial

#P0

def Pzero(tasaLlegada,tasaServicio,servidores):
	sumatoria=0
	for x in range(servidores):
		calculo = 1.0/factorial(x)*((tasaLlegada/tasaServicio)**x)
		sumatoria = sumatoria + calculo
	expresion = (1.0/factorial(servidores))*((tasaLlegada/tasaServicio)**servidores)*((servidores*tasaServicio)/(servidores*tasaServicio-tasaLlegada))
	resultado = 1.0/(sumatoria + expresion)
	return resultado

#Utilización Promedio p
def Sc(tasaLlegada,tasaServicio,servidores):
	return (float(tasaLlegada/(tasaServicio*servidores))*100)
#Factor o porcentaje ocioso del sistema
def ScOcio(tasaLlegada,tasaServicio,servidores):
	return (100-Sc(tasaLlegada,tasaServicio,servidores))

#Numero esperado de clientes en la cola (Lq)
def Lq(tasaLlegada,tasaServicio,servidores):
	return (((tasaLlegada*tasaServicio)*((tasaLlegada/tasaServicio)**servidores))/(factorial(servidores-1)*((servidores*tasaServicio-tasaLlegada)**2)))*Pzero(tasaLlegada,tasaServicio,servidores)

#Numero esperado de clientes recibiendo el servicio (Ls)
def Ls(tasaLlegada,tasaServicio,servidores):
	return tasaLlegada/tasaServicio

#Numero esperado de clientes en el sistema de colas (Lw)
def Lw(tasaLlegada,tasaServicio,servidores):
	return Lq(tasaLlegada,tasaServicio,servidores)+(tasaLlegada/tasaServicio)

#Valor esperado de tiempo que emplea un cliente en la cola (Wq)
def Wq(tasaLlegada,tasaServicio,servidores):
	return Lq(tasaLlegada,tasaServicio,servidores)/tasaLlegada

#Valor esperado del tiempo que emplea un cliente en el servicio (Ws)
def Ws(tasaLlegada,tasaServicio,servidores):
	return 1/tasaServicio

#Valor esperado del tiempo que emplea un cliente en recorrer el sistema (Ww)
def Ww(tasaLlegada,tasaServicio,servidores):
	return Wq(tasaLlegada,tasaServicio,servidores)+(1/tasaServicio)

#Probabilidad de que existan n clientes en la cola en estado estable
def ProbPn(tasaLlegada,tasaServicio,servidores,n):
	pn = 0
	if(n<=c):
		pn = (Pzero(tasaLlegada,tasaServicio,servidores)/factorial(n))*((tasaLlegada/tasaServicio)**n)
	else:
		pn = (Pzero(tasaLlegada,tasaServicio,servidores)/(factorial(servidores)*(servidores**(n-servidores))))*((tasaLlegada/tasaServicio)**n)
	return pn

#Probabilidad de que no se deba hacer cola
def ProbPnZero(tasaLlegada,tasaServicio,servidores,n):
	sumatoria = 0
	for x in range(servidores):
		sumatoria += ProbPn(tasaLlegada,tasaServicio,servidores,n)
	return sumatoria

#Probabilidad de que el tiempo empleado por un cliente en la cola (Wq) sea mayor a t unidades de tiempo
def ProbWq(tasaLlegada,tasaServicio,t,servidores,n):
	return (1-ProbPnZero(tasaLlegada,tasaServicio,servidores,n))*(exp((-servidores*tasaServicio)*(1-(tasaLlegada/tasaServicio))*t))

#Probabilidad de que el tiempo empleado por un cliente en recorrer el sistema (Ww) sea mayor a t unidades de tiempo
def ProbWw(tasaLlegada,tasaServicio,t,servidores,n):
	return exp(-tasaServicio*t)*((1+(Pzero(tasaLlegada,tasaServicio,servidores)*(((tasaLlegada/tasaServicio)**servidores)/(factorial(servidores)*(1-(tasaLlegada/tasaServicio))))))*((1-exp(-tasaServicio*t*(servidores-1-(tasaLlegada/tasaServicio))))/(servidores-1-(tasaLlegada/tasaServicio))))
 
def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce tu opción: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 	print("\nBienvenido, ingrese los datos manteniendo cuidado con las unidades de cada uno (horas, minutos, días)")
	print("1. Obtener datos generales")
	print("2. Obtener probabilidades")
	print("3. Salir")
     
	print ("Elige una opcion")
 
	opcion = pedirNumeroEntero()
 
	if opcion == 1:
		tasaLlegada = float(input("Ingrese el valor de la tasa de llegada (lambda): "))
		tasaServicio = float(input("Ingrese el valor de la tasa de servicio (u): "))
		servidores = int(input("Ingrese el número  de servidores (c): "))
		print 'P0 es:', Pzero(tasaLlegada,tasaServicio,servidores)
		print 'Tasa de uso del sistema: ' , Sc(tasaLlegada,tasaServicio,servidores),'%'
		print 'Tasa de ocio del sistema: ' , ScOcio(tasaLlegada,tasaServicio,servidores),'%'
		print 'Numero esperado de clientes en la cola (Lq): ', Lq(tasaLlegada,tasaServicio,servidores)
		print 'Numero esperado de clientes recibiendo servicio (Ls): ', Ls(tasaLlegada,tasaServicio,servidores)
		print 'Numero esperado de clientes en el sistema de colas (Lw): ', Lw(tasaLlegada,tasaServicio,servidores)
		print 'Valor esperado del tiempo que emplea un cliente en la cola (Wq): ', Wq(tasaLlegada,tasaServicio,servidores)
		print 'Valor esperado del tiempo que emplea un cliente en el servicio (Ws): ', Ws(tasaLlegada,tasaServicio,servidores)
		print 'Valor esperado del tiempo que emplea un cliente en recorrer el sistema (Ww): ', Ww(tasaLlegada,tasaServicio,servidores)
	elif opcion == 2:
		tasaLlegada = float(input("Ingrese el valor de la tasa de llegada : "))
		tasaServicio = float(input("Ingrese el valor de la tasa de servicio : "))
		t = float(input("Ingrese el valor de t (tiempo): "))
		n = float(input("Ingrese el valor de n: "))
		servidores = int(input("Ingrese el número  de servidores (c): "))
		print 'P0 es:', Pzero(tasaLlegada,tasaServicio,servidores)
		print 'Probabilidad de que no hayan clientes en la cola es:', ProbPnZero(tasaLlegada,tasaServicio,servidores,n)
		print 'Probabilidad de que hayan ', n , 'clientes en la cola en estado estable es: ',ProbPn(tasaLlegada,tasaServicio,n),'%'
		print 'Probabilidad de que el tiempo empleado por un cliente en la cola (Wq) sea mayor a ', t,' es: ',ProbWq(tasaLlegada,tasaServicio,t,servidores,n),'%'
		print 'Probabilidad de que el tiempo empleado por un cliente en recorrer el sistema (Ww) sea mayor a ', t,' es: ',ProbWw(tasaLlegada,tasaServicio,t,servidores,n),'%'

	elif opcion == 3:
		salir = True
	else:
		print ("Introduce un numero entre 1 y 3")

print ("Fin")
    