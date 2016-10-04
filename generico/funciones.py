def suma(a,b):
	print("%d + %d = %d" %(a,b,a+b))

def devuelveLista():
	a = ["Hola", 3, 3.8]
	return a

def dosFrases():
	lista = []
	print("Introduce una frase")
	lista.append(raw_input())
	print("Introdue otra frase")
	lista.append(raw_input())

	for i in lista:
		print(i),

	print("Voy a quitar las palabras repetidas en la frase uno \n")

	f1 = lista[0].split()
	f2 = lista[1].split()

	for i in f1:
		for j in f2:
			if i.upper() == j.upper():
				del f1[(f1.index(i))]

	lista[0] = " ".join(f1)
	print lista

def pideLista():
	
	a = []
	condicion = 0

	while condicion == 0:
		print("Introduce un elemento para introducir en la lista \n si quieres introducir cadenas tienes que ponerlo entre comillas \" \" ")
		a.append(input())
		print("0 - Introducir mas")
		print("1 - Terminar")
		condicion = input()

	a.sort()

	print(a)

def strToList():
	print("Introduce una frase")
	a = raw_input()
	lista = a.split()
	print(lista)
	print("Longitud de la lista %d" %(len(lista)))
	lista.sort()
	print(lista)

def tuplePerson():
	a = ("Alvaro", "Cardador", 23, 74.0, "30990565C")
	return a

def intercambiarTuplas():
	a = ("Alvaro", "Cardador", 23, 74.0, "30990565C")
	b = ("Paco", "Galvez")

	a,b = b,a

	print(a)
	for i in b:
		print(i),

def tuplaTeclado():
	a = ()
	b = []

	for i in range(1,11):
		print("Introduce un valor para aniadir a la tupla: \n")
		b = raw_input().join("")
		a = a + tuple(b)
		print(a)

def devuelveTupla():
	a = ("Alvaro", "Cardador", 23, 74.0, "30990565C")
	return a


def parametrosVariables(*args):
	for arg in args:
		print arg, " tipo = ", type(arg)

def listaPalabras(a):

	b = []
	suma = 0
	nElem = 0
	maxLen = 0
	minLen = 1000

	for i in a:
		b.append(len(i))
		suma = suma + len(i)
		nElem = nElem + 1
		
		if len(i) > maxLen:
			maxLen = len(i)

		if len(i) < minLen:
			minLen = len(i)

	b.append("La media de letras es %d" %(suma/nElem))
	b.append("El valor mas corto es de %d" %(minLen))
	b.append("El valor mas largo es de %d" %(maxLen))
	print(b)
