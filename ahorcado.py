import random as rd

def palabraAleatoria():
	palabras = ["Informatica", "Programacion", "Analisis", "Codigo"
	, "Programa", "Software", "Hardware", "Binario", "Lenguaje"]
	return palabras[rd.randint(0, len(palabras) - 1)].lower()
	
def ahorcado():
	palabra = palabraAleatoria()
	adivino = False
	espacios = [None] * len(palabra)
	for i in range(len(espacios)):
		espacios[i] = "_"
	vidas = 6
	while(vidas > 0 and adivino == False):
		print("\nTrate de adivinar la palabra. Tiene " + str(vidas) + " vidas")
		print("Ingrese una letra o la palabra completa")
		print("Ingrese el numero cero (0) en cualquier momento para salir")
		print("\n" + str(espacios))
		print()
		puntos = 0
		opcion = input().lower().strip()
		if opcion == "0":
			adivino = "salir"
		elif(len(opcion) > 1):
			if(opcion == palabra):
				adivino = True
			else:
				vidas -=1
				if vidas != 0:
					print("'" + opcion + "' no es la palabra secreta. Sigue intentandolo")
					
		else:
			for i in range(len(espacios)):
				if opcion == palabra[i]:
					espacios[i] = opcion
					puntos +=1	
			if "_" not in espacios:
				print(espacios)
				print()
				adivino = True
			if puntos != 0:
				print("Bien. '" + opcion + "' aparece en " + str(puntos) + " espacios")
				continue
			else:
				vidas -=1
				if vidas != 0:
					print("Sigue intentandolo. '" + opcion + "' no esta dentro de la palabra secreta")
				
	resultado(adivino,palabra)

def resultado(adivino, palabra):
	if adivino == True:
		print("\nFelicitaciones!, la palabra era '" + palabra + "'")
	elif adivino == False:
		print("\nLo siento. No adivinaste. La palabra era '" + palabra + "'")
			
def salir():
	print("(1): Jugar")
	print("(2): Salir")
	opcion = input()
	return opcion
	
while True:
	salida = salir()
	if salida == "1":
		ahorcado()
	elif salida == "2":
		break
	else:
		print("Ingrese una opcion valida")
