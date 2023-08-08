class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self):
        print("La cordenada en x es: ", self.x)
        print("La cordenada en y es: ", self.y)

    def mover(self):
        self.x = self.x + 3
        self.y = self.y + 6
        return self.x, self.y


    def calcular_distancia(self, otro_punto):
        distancia_x = self.x - otro_punto.x
        distancia_y = self.y - otro_punto.y
        distancia = ((distancia_x ** 2) + (distancia_y ** 2)) ** 0.5
        return distancia

punto1 = Punto(5, 3)
punto2 = Punto(8, 9)

punto1.mostrar()

movidas = punto1.mover()
print("Nuevas coordenadas después de mover:", movidas)


distancia = punto1.calcular_distancia(punto2)
print("Distancia entre los puntos:", distancia)

        