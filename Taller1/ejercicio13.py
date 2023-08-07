def calcular_operaciones(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    return suma, resta, multiplicacion, division

print("Ingrese el primer número:")
numero1 = float(input())

print("Ingrese el segundo número:")
numero2 = float(input())

suma, resta, multiplicacion, division = calcular_operaciones(numero1, numero2)

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)