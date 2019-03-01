#Algoritmo que lea 10 números y determine cuántos números fueron positivos , cuántos negativos y cuantos fueron cero.
#Vamos a definir tres contadores ; uno para los positivos , uno para los negativos y finalmente otro para los ceros.
def count_Positive(NumList):
    Positive_count = 0
    for j in range(Number):
        if(NumList[j] > 0):
            Positive_count = Positive_count + 1
    return Positive_count

def count_Negative(NumList):
    Negative_count = 0
    for j in range(Number):
        if(NumList[j] % 2 != 0):
            Negative_count = Negative_count + 1
    return Negative_count

def count_zeroes(NumList):
    zeroes_count = 0
    for j in range(Number):
        if (NumList[j] == 0):
            zeroes_count = zeroes_count + 1
    return zeroes_count

NumList = []
Number = int(input("Bienvenido! Por favor Ingrese el número de números que quieres ingresar para evaluar: "))
for i in range(1, Number + 1):
    value = int(input("Por favor ingresa el valor del numero %d : " %i))
    NumList.append(value)

Positive_cnt = count_Positive(NumList)
Negative_cnt = count_Negative(NumList)
zeroes_cnt = count_zeroes(NumList)
print("\nEl número total de números positivos es :  ", Positive_cnt)
print("El número total de números negativos es : ", Negative_cnt)
print("El número total de zeros es: ",zeroes_cnt)
# Desarrollado por Pedro Gómez / ID:000396221
        
