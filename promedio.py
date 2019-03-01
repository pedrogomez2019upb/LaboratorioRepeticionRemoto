#Programa que saque el promedio de n notas
n = int(input("Bienvenido ! Este programa te ayuda a calcular el promedio de n numeros. ¿Cuántas notas vas a promediar?: "))
total_suma = 0
#Ahora vamos a poner una condicional for para que cumpla las condicionales
for n in range(n):
    numbers = float(input("Ingresa el valor : "))
    total_suma += numbers
promedio = total_suma/n
print("El promedio de las notas es de {}".format(promedio))
#Creado por Pedro Gómez / ID:000396221