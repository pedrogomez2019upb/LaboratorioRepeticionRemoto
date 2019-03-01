#Crear un algoritmo que sepa si un número entero a es par 
#Primero hacemos que agrergue el número a
a=input("Bienvenido ! Vamos a evaluar si tu número es par. Por favor ingresa el primer número entero: ")
#Revisamos si primero el número es 0 o con decimal 
if (a == 0 or a=float):
    print("El número es decimal o es 0.")
else:
    if a % 2:
        print ("El número {} es par. Gracias por utilizar el programa.".format(a))
    else:
        print ("El número {} es impar. Gracias por utilizar el programa.".format(a))
