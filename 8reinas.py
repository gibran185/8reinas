#! /usr/bin/env python
# -*- encoding: utf-8 -*-
import sys
tablero = []
tamanio = 8
count = 0

 #Metodo para determinar si la casilla esta en zona de peligro por una reina
def bad_cas(fila, col):
	#Se recorre el arreglo tablero, los elementos se van guardando en i & j en cada iteración
    for (i, j) in tablero:
        if fila == i: return True
        if col == j: return True
        if abs(fila - i) == abs(col - j): return True

    return False
    
def lugar_reina(fila, num):
	if fila > tamanio:
		global count
		count +=1
		if count == num:
			print count
			print tablero
			sys.exit(0)
	else:
		for colum in range(1, tamanio + 1):
			if not bad_cas(fila, colum):
				tablero.append((fila, colum))
				lugar_reina(fila + 1, num)
				tablero.remove((fila,colum))

if __name__ == "__main__":
	num = input("Ingrese la respuesta que desea observar (1-92):")
	if num > 92:
		print ("Sólo hay 92 respuestas posibles para el problema de las 8 reinas")

	lugar_reina(1, num)