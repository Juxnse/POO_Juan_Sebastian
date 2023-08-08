class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        return 3.14159 * self.radio ** 2 

    def calcular_perimetro(self):
        return 2 * 3.14159 * self.radio 

    def punto_pertenece(self, punto):
        distancia_x = punto[0] - self.centro[0]
        distancia_y = punto[1] - self.centro[1]
        distancia_al_cuadrado = distancia_x ** 2 + distancia_y ** 2
        return distancia_al_cuadrado <= self.radio ** 2


punto = (3, 4)
centro = (0, 0)
radio = 5
circulo1 = Circulo(centro, radio)

if circulo1.punto_pertenece(punto):
    print(f"El punto {punto} pertenece al círculo.")
else:
    print(f"El punto {punto} no pertenece al círculo.")
