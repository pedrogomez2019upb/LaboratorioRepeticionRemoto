#Crear un algoritmo que sepa si un número entero a es par 
#Primero hacemos que agrergue el número a
a=int(input("Bienvenido ! Vamos a evaluar si tu número es par. Por favor ingresa el primer número entero: "))
#Revisamos si primero el número es 0 o con decimal 
if (a % 2) == 0:
    print ("El número {} es par. Muchas gracias por utilizar el programa".format(a))
else:
    print ("El número {} es impar. Muchas gracias por utilizar el programa.".format(a))

#Desarrollado por Pedro Gómez / ID : 000396221
