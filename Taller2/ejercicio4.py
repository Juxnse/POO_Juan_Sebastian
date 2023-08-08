class Rectangulo:
    def __init__(self, punto_esquina_1, punto_esquina_2, punto_esquina_3, punto_esquina_4):
        self.punto_esquina_1 = punto_esquina_1
        self.punto_esquina_2 = punto_esquina_2
        self.punto_esquina_3 = punto_esquina_3
        self.punto_esquina_4 = punto_esquina_4

    def calcular_distancia(self, punto1, punto2):
        return ((punto2[0] - punto1[0])**2 + (punto2[1] - punto1[1])**2)**0.5

    def calcular_perimetro(self):
        lado1 = self.calcular_distancia(self.punto_esquina_1, self.punto_esquina_2)
        lado2 = self.calcular_distancia(self.punto_esquina_2, self.punto_esquina_3)
        lado3 = self.calcular_distancia(self.punto_esquina_3, self.punto_esquina_4)
        lado4 = self.calcular_distancia(self.punto_esquina_4, self.punto_esquina_1)

        perimetro = lado1 + lado2 + lado3 + lado4
        return perimetro

    def calcular_area(self):
        lado1 = self.calcular_distancia(self.punto_esquina_1, self.punto_esquina_2)
        lado2 = self.calcular_distancia(self.punto_esquina_2, self.punto_esquina_3)

        area = lado1 * lado2
        return area

    def todo_cuadrado_es_rectangulo_pero_no_todo_rectangulo_es_cuadrado(self):
        lado1 = self.calcular_distancia(self.punto_esquina_1, self.punto_esquina_2)
        lado2 = self.calcular_distancia(self.punto_esquina_2, self.punto_esquina_3)
        lado3 = self.calcular_distancia(self.punto_esquina_3, self.punto_esquina_4)
        lado4 = self.calcular_distancia(self.punto_esquina_4, self.punto_esquina_1)

        if lado1 == lado2 == lado3 == lado4:
            return "El rectángulo es un cuadrado."
        else:
            return "El rectángulo no es un cuadrado."


rectangulo1 = Rectangulo((0, 0), (2, 0), (2, 2), (0, 2))


perimetro = rectangulo1.calcular_perimetro()
print("El perímetro del rectángulo es:", perimetro)


area = rectangulo1.calcular_area()
print("El área del rectángulo es:", area)


cuadrado_info = rectangulo1.todo_cuadrado_es_rectangulo_pero_no_todo_rectangulo_es_cuadrado()
print(cuadrado_info)

