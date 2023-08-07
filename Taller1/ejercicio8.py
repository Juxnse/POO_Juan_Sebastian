def invertir_lista(lista):
    lista_invertida = []
    for i in lista:
        lista_invertida.insert(0, i)
    return lista_invertida

lista = [1, 2, 3, 4, 5]
lista_invertida = invertir_lista(lista)
print(lista_invertida)

        