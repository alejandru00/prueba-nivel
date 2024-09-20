
from superclase.vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        Vehiculo.__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return Vehiculo.__str__() + f", Tipo: {self.tipo}"
    
