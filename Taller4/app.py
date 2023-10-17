from modelo.tienda_libros import TiendaLibros
from UIConsola import UIConsola

tienda = TiendaLibros()
ui = UIConsola()

while True:
    print("1. Agregar libro al catálogo")
    print("2. Agregar libro al carrito")
    print("3. Retirar libro del carrito")
    print("4. Calcular total del carrito")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ui.adicionar_un_libro_a_catalogo(tienda)
    elif opcion == "2":
        ui.agregar_libro_a_carrito_de_compras(tienda)
    elif opcion == "3":
        ui.retirar_libro_de_carrito_de_compras(tienda)
    elif opcion == "4":
        total = tienda.carrito.calcular_total()
        print(f"El total del carrito es: ${total:.2f}")
    elif opcion == "5":
        break
