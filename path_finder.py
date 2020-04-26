def encuentra_el_camino(lado_del_tablero,pos_actual,pos_inicial,pos_objetivo,tablero,lista_de_herencias):
	encontrado_el_final=True
	pos_actual = pos_inicial
	dar_valores_alrededor(lado_del_tablero,pos_actual,pos_objetivo,pos_inicial,tablero,lista_de_herencias)
	while encontrado_el_final:
		el_mas_pequeño = buscar_el_menor(tablero)
		try:
			pos_actual = tablero.index(el_mas_pequeño)
		except ValueError:
			print("ese es el camino")
			break
		dar_valores_alrededor(lado_del_tablero,pos_actual,pos_objetivo,pos_inicial,tablero,lista_de_herencias)
	antecesor = lista_de_herencias[pos_objetivo]
	#tablero[tablero.index(2)] = "+"
	while antecesor != 0:
		tablero[antecesor] = "+"
		antecesor = lista_de_herencias[antecesor]


def dar_valores_alrededor(lado,pos_actual,pos_objetivo,pos_inicial,tablero,lista_de_herencias):
	tablero[pos_actual] = "z"
	simbolos = ["z","@","$"]
	try:
		if not(tablero[pos_actual + 1] in simbolos) :
			tablero[pos_actual + 1] = calcular_distancia(lado,pos_actual + 1,pos_objetivo) + calcular_distancia(lado,pos_actual + 1,pos_inicial)
			lista_de_herencias[pos_actual + 1] = pos_actual
		elif tablero[pos_actual + 1] == "@":
			tablero[pos_actual + 1] = 2
			lista_de_herencias[pos_actual + 1] = pos_actual
			encontrado_el_final = False
	except IndexError:
		pass
	try:
		if not(tablero[pos_actual - 1] in simbolos) :
			lista_de_herencias[pos_actual - 1] = pos_actual
			tablero[pos_actual - 1] = calcular_distancia(lado,pos_actual - 1,pos_objetivo) + calcular_distancia(lado,pos_actual - 1,pos_inicial)
		elif tablero[pos_actual - 1] == "@":
			tablero[pos_actual - 1] = 2
			lista_de_herencias[pos_actual - 1] = pos_actual
			encontrado_el_final = False
	except IndexError:
		pass
	try:
		if not(tablero[pos_actual + lado] in simbolos):
			tablero[pos_actual + lado] = calcular_distancia(lado,pos_actual + lado,pos_objetivo) + calcular_distancia(lado,pos_actual + lado,pos_inicial)
			lista_de_herencias[pos_actual + lado] = pos_actual
		elif tablero[pos_actual + lado] == "@":
			tablero[pos_actual + lado] = 2
			lista_de_herencias[pos_actual + lado] = pos_actual
			encontrado_el_final = False
	except IndexError:
		pass		
	try:
		if not(tablero[pos_actual - lado] in simbolos):
			lista_de_herencias[pos_actual - lado] = pos_actual
			tablero[pos_actual - lado] = calcular_distancia(lado,pos_actual - lado,pos_objetivo) + calcular_distancia(lado,pos_actual - lado,pos_inicial)
		elif tablero[pos_actual - lado] == "@":
			tablero[pos_actual - lado] = 2
			lista_de_herencias[pos_actual - lado] = pos_actual
			encontrado_el_final = False
	except IndexError:
		pass

def calcular_distancia(lado,posicion,pos_objetivo):
	distancia = pos_objetivo - posicion
	distancia_x = distancia%lado
	if distancia < 0 :
		distancia = -distancia
	distancia_y = distancia//lado
	distancia_final = distancia_x**2 + distancia_y**2
	return distancia_final

def buscar_el_menor(a):
	menor = 1000000000
	for i in a:
		if type(i) == int:
			if i != 0 and i != 1:
				if i < menor:
					menor = i
	return menor