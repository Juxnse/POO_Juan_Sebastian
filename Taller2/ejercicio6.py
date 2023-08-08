class Carta:
    PINTA_CORAZON = "Corazón"
    PINTA_DIAMANTE = "Diamante"
    PINTA_TREBOL = "Trébol"
    PINTA_PICA = "Pica"

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

carta1 = Carta(10, Carta.PINTA_CORAZON)

# Imprimir propiedades de la carta
print("Valor:", carta1.valor)
print("Pinta:", carta1.pinta)
