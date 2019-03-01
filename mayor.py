#Algoritmo que lea 10 números y determine cuántos números fueron positivos , cuántos negativos y cuantos fueron cero.
#Vamos a definir tres contadores ; uno para los positivos , uno para los negativos y finalmente otro para los ceros.
def count_positivos(NumList):
    positivos = 0
    for j in range(Number):
        if(NumList[j] >= 0):
            positivos = positivos + 1
    return positivos

def count_negativos(NumList):
    negativos = 0
    for j in range(Number):
        if(NumList[j] % 2 != 0):
            negativos = negativos + 1
    return negativos

def count_ceros(NumList):
    ceros = 0
    for j in range(Number):
        if(NumList[j] == 0):
            ceros = ceros + 1
    return ceros

NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

positivos_cnt = count_positivos(NumList)
negativos_cnt = count_negativos(NumList)
ceros_cnt = count_ceros(NumList)
print("\nTotal Number of Positive Numbers in this List =  ", positivos_cnt)
print("Total Number of Negative Numbers in this List = ", negativos_cnt)
print ("El número total de ceros en la lista es {}".format(ceros_cnt))
# Desarrollado por Pedro Gómez / ID:000396221
        
