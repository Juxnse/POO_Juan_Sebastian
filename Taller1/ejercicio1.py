def nombre():
  Nombre = str(input("Ingrese su nombre: "))
  return Nombre

def apellido():
  Apellido = str(input("Ingrese su apellido: "))
  return Apellido

nom = nombre()
ape = apellido()
print("Su nombre completo es: ", nom, ape)