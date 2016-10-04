import random
import string
def devPalabras():
	palabras = [];
	# En primer lugar debemos de abrir el fichero que vamos a leer.
	# Usa 'rb' en vez de 'r' si se trata de un fichero binario.
	infile = open('palabras.txt', 'r')
	# Mostramos por pantalla lo que leemos desde el fichero
	#print('>>> Lectura del fichero linea a linea')
	for line in infile:
		aux = line.split()
		for aux_aux in aux:
			if aux_aux not in palabras:
				palabras.append(aux_aux)
	# Cerramos el fichero.
	infile.close()
	return palabras

def seleccionaElemento(lista):
	return random.choice(lista)

def introLetra():
	letra = ""
	
	print("Introduce una letra")
	letra = raw_input()
	
	while len(letra) > 1 or len(letra) < 1 or letra not in string.letters:
		print("Introduce UNA SOLA letra")
		letra = raw_input()
	
	return letra

def buscaLetra(letra, cadena):
	indices = []
	
	for i in range(0, len(cadena)):
		if string.upper(letra) == string.upper(cadena[i]):
			indices.append(i)

	return indices