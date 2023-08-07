import random

def lista_pares(n):
    lista = []
    for i in range(n):
        numero = random.randrange(2, 101, 2)
        lista.append(numero)
    return lista

print("Ingrese cuántos números pares aleatorios desea obtener:")
n = int(input())

numeros_pares = lista_pares(n)
print(numeros_pares)
