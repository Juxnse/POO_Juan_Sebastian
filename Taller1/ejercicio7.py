def encontrar_numero(lista):
    numMayor = lista[0]
    numMenor = lista[0]
    for i in lista:
        if i >= i:
            numMayor = i
            print(numMayor)

        elif i <= i:
            numMenor = i
            print(numMenor)

    return numMayor, numMenor

lista = [1,2,3,4,5]
resultado = encontrar_numero(lista)
print("Número mayor:", resultado[0])
print("Número menor:", resultado[1])
