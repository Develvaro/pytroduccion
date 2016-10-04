from palabras import *
from time import time

palabras = devPalabras()

palabra = seleccionaElemento(palabras)

pista = ""

aciertos = 0
fallos = 0

for i in palabra:
	pista = pista + "-"

print(pista)

tiempo_inicial = time()

while 1:

	letra = introLetra()

	print("Letra introducida "),
	print(letra)

	letras = buscaLetra(letra,palabra)

	aciertos = aciertos + len(letras)

	if len(letras) == 0:
		fallos = fallos + 1

	for i in letras:
		pista = pista[0:i] + letra + pista[i+1:]

	print(pista)
	print("Aciertos: "),
	print(aciertos)

	print("Fallos: "),
	print(fallos)

	if "-" not in pista:
		break

tiempo_final = time()

tiempo_ejecucion = tiempo_final - tiempo_inicial

print("Muy bien, la palabra era %s" %(palabra))
print("Has tardado %f segundos" %(tiempo_ejecucion))
