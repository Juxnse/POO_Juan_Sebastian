class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, cantidad):
        self.balance += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
        else:
            print("Saldo insuficiente.")

    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota

    def mostrar_detalles(self):
        print("Número de cuenta:", self.numero_cuenta)
        print("Propietarios:", ", ".join(self.propietarios))
        print("Balance:", self.balance)

# Crear una cuenta bancaria
numero_cuenta = "03007104807"
propietarios = ["Felipe Ogaza", "Juliana Holguin"]
balance_inicial = 10000
cuenta1 = CuentaBancaria(numero_cuenta, propietarios, balance_inicial)

# Mostrar detalles de la cuenta
cuenta1.mostrar_detalles()

# Realizar operaciones en la cuenta
cuenta1.depositar(500)
cuenta1.retirar(300)
cuenta1.aplicar_cuota_manejo()

# Mostrar detalles actualizados de la cuenta
cuenta1.mostrar_detalles()
