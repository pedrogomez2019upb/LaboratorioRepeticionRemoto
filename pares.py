#Crear un algoritmo que sepa si un número entero a es par 
#Primero hacemos que el usuario pueda ingresar cuantos valores quiere evaluar
a=int(input("Bienvenido ! Vamos a evaluar si los números que quieres revisar son pares, si es impar el programa para. Ingresa la cantidad de valores que quieres revisar: "))
#Vamos a implementar la condicional for para ingersar los números a revisar
contarPares = 0
for y in range (1,a,1):
    z=int(input("Ingresa el número a revisar: "))
#Ponemos una condicional if y elif para que siga el bucle
    if z % 2 == 0:
        contarPares = contarPares + 1
        print("El número {} es par. Sigue ingresando valores.".format(z))
    elif z % 2!=0:
        print ("El número {} es impar. Gracias por utilizar el programa.".format(z))
        break
#Desarrollado por Pedro Gómez / ID : 000396221
