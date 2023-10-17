class UIConsola:
    def adicionar_un_libro_a_catalogo(self, tienda):
        isbn = input("ISBN del libro: ")
        titulo = input("Título del libro: ")
        precio = float(input("Precio del libro: "))
        existencias = int(input("Existencias del libro: "))
        libro = tienda.adicionar_libro_a_catalogo(isbn, titulo, precio, existencias)
        print(f"Libro añadido al catálogo: {libro}")

    def agregar_libro_a_carrito_de_compras(self, tienda):
        isbn = input("ISBN del libro a agregar al carrito: ")
        cantidad = int(input("Cantidad de unidades a agregar: "))
        try:
            tienda.agregar_libro_a_carrito(isbn, cantidad)
            print(f"Libro añadido al carrito de compras.")
        except Exception as e:
            print(f"Error: {e}")

    def retirar_libro_de_carrito_de_compras(self, tienda):
        isbn = input("ISBN del libro a retirar del carrito: ")
        tienda.retirar_item_de_carrito(isbn)
        print(f"Libro retirado del carrito de compras.")
