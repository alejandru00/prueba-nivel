
from superclase.vehiculo import Vehiculo

class Coche(Vehiculo):
	def __init__(self, color, ruedas, velocidad, cilindrada):
		Vehiculo.__init__(self, color, ruedas)
		self.velocidad = velocidad
		self.cilindrada = cilindrada
		
	def __str__(self):  
		return super().__str__() + f", Velocidad: {self.velocidad} km/h, Cilindrada: {self.cilindrada} cc"

