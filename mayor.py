#Algoritmo que lea 10 números y determine cuántos números fueron positivos , cuántos negativos y cuantos fueron cero.
#Vamos a hacer un for para que pueda ingresar la cantidad que quiera evaluar
NumList = []
Positive_count = 0
Negative_count = 0
#Ingresa el número de números que quiere evaluar
Number = int(input("Bienvenid@! Vamos a evaluar los números que quieras para ver si son positivos , negativos o igual a cero: Ingresa la cantidad que quieres evaluar: "))
for i in range(1, Number + 1):
    value = int(input("Por favor ingresa el valor de número %d : " %i))
    NumList.append(value)

for j in range(Number):
    if(NumList[j] >= 0):
        Positive_count = Positive_count + 1
    else:
        Negative_count = Negative_count + 1

print("\nTotal Number of Positive Numbers in this List =  ", Positive_count)
print("Total Number of Negative Numbers in this List = ", Negative_count)
# Desarrollado por Pedro Gómez / ID:000396221
        
