def suma_lista(lista):
  sum = 0
  for i in lista:
    sum = sum + i
  return sum

lista = [1,45,8643,654,789,1234]
print("La suma de la lista es:",suma_lista(lista))