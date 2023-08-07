def calcular_media(lista):
    if len(lista) == 0:
        return None
    suma = sum(lista)
    media = suma / len(lista)
    return media

numeros = [10, 20, 30, 40, 50]
media_calculada = calcular_media(numeros)
print("La media aritmética es:", media_calculada)