#Programa que saque el promedio de n notas con la función while
#En este caso vamos a utilizar 0 para que el usuario pare el programa
print("Bienvenido ! Este programa te permite saber la suma y el promedio de los números ingresados. Si quieres terminar de ingresar números , presiona 0.")

count = 0
sum = 0.0
number = 1
#Simplemente ingresamos while para que tome la condicional y haga el procedimiento matemático
while number != 0:
	number = int(input("Ingresa el valor (para cancelar escribe 0)"))
	sum = sum + number
	count += 1

if count == 0:
	print("Ingresa un valor si de verdad queires continuar utilizando el")
else:
	print("La suma y el promedio respectivamente son: ", sum / (count-1), sum)
#Creado por Pedro Gómez / ID:000396221