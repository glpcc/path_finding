import time
import keyboard
import path_finder
from random import randint
def crear_tablero():
	for i in range(lado**2):
		if i%lado == 0 or i%lado == lado -1:
			tablero.append("$")
			tablero_de_herencias.append(0)
		elif  0<i<lado or (lado**2 - lado)<i<lado**2:
			tablero.append("$")	
			tablero_de_herencias.append(0)
		elif i == 45:
			tablero.append(1)
			tablero_de_herencias.append(0)	
		else:
			a = randint(1,10)
			if a > 7:
				tablero.append("$")
				tablero_de_herencias.append(0)
			else:
				tablero.append(0)
				tablero_de_herencias.append(0)

def crear_objetivo():
	global posicion
	global posicion_objetivo 
	posicion_objetivo = posicion
	tablero[posicion] = "@"
def crear_inicio():
	global posicion 
	global posicion_inicio
	posicion_inicio = posicion
	tablero[posicion] = "%"
def crear_bloqueo():
	global posicion 
	tablero[posicion] = "$"

def mover_derecha():
	global posicion
	if tablero[posicion] != "$" and tablero[posicion] != "@" and tablero[posicion] != "%":
		tablero[posicion] = 0
	posicion += 1
	if tablero[posicion] != "$" and tablero[posicion] != "@":
		tablero[posicion] = 1
		dibujar_tablero()
	else:
		posicion -= 1


def mover_izquierda():
	global posicion
	if tablero[posicion] != "$" and tablero[posicion] != "@" and tablero[posicion] != "%":
		tablero[posicion] = 0
	posicion -= 1
	if tablero[posicion] != "$" and tablero[posicion] != "@":
		tablero[posicion] = 1
		dibujar_tablero()
	else:
		posicion += 1

def mover_abajo():
	global posicion
	if tablero[posicion] != "$" and tablero[posicion] != "@" and tablero[posicion] != "%":
		tablero[posicion] = 0
	posicion += lado
	if tablero[posicion] != "$" and tablero[posicion] != "@":
		tablero[posicion] = 1
		dibujar_tablero()
	else:
		posicion -= lado

def mover_arriba():
	global posicion
	if tablero[posicion] != "$" and tablero[posicion] != "@" and tablero[posicion] != "%":
		tablero[posicion] = 0
	posicion -= lado
	if tablero[posicion] != "$" and tablero[posicion] != "@":
		tablero[posicion] = 1
		dibujar_tablero()
	else:
		posicion += lado

def dibujar_tablero():
	for i in range(len(tablero)):
		if (i +1)% lado != 0:
			print (tablero[i],end=" ")
		elif (i+1) == 0:
			print (tablero[i],end=" ")
		else:
			print(tablero[i])
	for i in range(5):
		print()
def limpiar_el_tablero():
	for i in tablero:
		if i != "+" and i != "$":
			tablero[tablero.index(i)]=0
def reiniciar():
	for i in tablero:
		if i != "$":
			tablero[tablero.index(i)]= 0

tablero_de_herencias= []
tablero  = []
lado = 10
posicion = 45
posicion_objetivo = 0
posicion_inicio = 0
lado=int(input("cuanto mide el lado:"))
posicion = 45 +lado
crear_tablero()
dibujar_tablero()


while True:
	if keyboard.is_pressed('w'):
		mover_arriba()
		time.sleep(0.5)
	elif keyboard.is_pressed('s'):
		mover_abajo()
		time.sleep(0.5)
	elif keyboard.is_pressed('a'):
		mover_izquierda()
		time.sleep(0.5)
	elif keyboard.is_pressed('d'):
		mover_derecha()
		time.sleep(0.5)
	elif keyboard.is_pressed('b'):
		crear_bloqueo()
	elif keyboard.is_pressed('f'):
		crear_objetivo()
		time.sleep(0.5)
	elif keyboard.is_pressed('i'):
		crear_inicio()
		time.sleep(0.5)
	elif keyboard.is_pressed('z'):
		path_finder.encuentra_el_camino(lado,posicion,posicion_inicio,posicion_objetivo,tablero,tablero_de_herencias)
		time.sleep(0.5)
		limpiar_el_tablero()
		dibujar_tablero()
	elif keyboard.is_pressed('r'):
		reiniciar()
		time.sleep(0.5)