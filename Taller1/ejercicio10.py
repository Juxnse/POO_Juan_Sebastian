def factorial(a):
    if a == 0 or a == 1:
        resultado = 1
        print(resultado)
    elif a > 1:
        resultado = a * factorial(a - 1)
        print(resultado)
    return resultado

igual = factorial(4)
print("La multiplicacion es: ",igual)
