#Algoritmo que permita determinar si un número entero es mayor a cero
#Primero vamos a crerar una variable X para que reciba un valor 
x=eval(input("Bienvenido! Vamos a evaluar el número ingresado para saber si es mayor a cero. Por favor ingresa un número entero: "))
#Se va a añadir un chequeo del número ingresado para ver si es entero o es 0
if type(x) == float or x == 0:
    print("El número no es entero o es igual a cero. Gracias por utilizar el programa.")
else:
    if x > 0:
        print ("El número {} es mayor a cero. Gracias por utilizar el programa.".format(x))
    else:
        print("El número {} es menor a cero. Gracias por utilzar el programa.".format(x))
# Desarrollado por Pedro Gómez / ID:000396221
        
