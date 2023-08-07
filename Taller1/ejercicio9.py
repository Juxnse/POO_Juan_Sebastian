def crear_matriz(lista):
    matriz = []
    for i in lista:
        fila = [i, i + 1, i + 2, i + 3, i + 4]
        matriz.append(fila)
    return matriz

lista = [7, 8, 9, 10]
matriz = crear_matriz(lista)
for fila in matriz:
    print(fila)

