
from subclase.bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(self, color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f", Velocidad: {self.velocidad} km/h, Cilindrada: {self.cilindrada} cc"