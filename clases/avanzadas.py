import math
class OperacionesAvanzadas:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def leerNumeros(self):
        self.num1 = float(input("Ingrese el número base: "))
        self.num2 = float(input("Ingrese el exponente: "))

    def elevarPotencia(self):
        return self.num1 ** self.num2
    
    def raizCuadrada(self):
        return math.sqrt(self.num1)
# Espacio para que los colaboradores agreguen la raíz cuadrada