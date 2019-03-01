#Algoritmo que lea 10 números y determine cuántos números fueron positivos , cuántos negativos y cuantos fueron cero.
#Vamos a hacer un for para que pueda ingresar la cantidad que quiera evaluar
NumList = []
positivos = 0
negativos = 0
#Ingresa el número de números que quiere evaluar
Number = int(input("Bienvenid@! Vamos a evaluar los números que quieras para ver si son positivos , negativos o igual a cero: Ingresa la cantidad que quieres evaluar: "))
for i in range(1, Number + 1):
    value = int(input("Por favor ingresa el valor de número %d : " %i))
    NumList.append(value)

for j in range(Number):
    if(NumList[j] >= 0):
        postivos = positivos + 1
    else:
        negativos = negativos + 1

print("\nLos números postivios de la lista fueron =  ", postivos)
print("Los números negativos de la lista fueron = ", negativos)
# Desarrollado por Pedro Gómez / ID:000396221
        
