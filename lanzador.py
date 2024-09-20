
from subclase.coche import Coche
from subclase.bicicleta import Bicicleta
from subsubclase.motocicleta import Motocicleta
from subsubclase.camioneta import Camioneta

def catalogar(vehiculos, ruedas=None):
    if ruedas is not None:
        contador = sum(1 for v in vehiculos if v.ruedas == ruedas)
        print(f"Se han encontrado {contador} vehículos con {ruedas} ruedas:")

    for vehiculo in vehiculos:
        if ruedas is None or vehiculo.ruedas == ruedas:
            print(f"{type(vehiculo).__name__}: {vehiculo}")

def main():
    vehiculos = []

    vehiculo1 = Coche("Blanco", 4, 150, 1800)       # color, ruedas, velocidad, cilindrada
    vehiculos.append(vehiculo1)
    print(vehiculo1)

    vehiculo2 = Bicicleta("Azul", 2, "Urbana")      # color, ruedas, tipo
    vehiculos.append(vehiculo2)
    print(vehiculo2)

    vehiculo3 = Motocicleta("Negra", 2, "Deportiva", 180, 900)      # color, ruedas, tipo, velocidad, cilindrada
    vehiculos.append(vehiculo3)
    print(vehiculo3)

    vehiculo4 = Camioneta("Gris", 4, 100, 2200, 1500)       # color, ruedas, velocidad, cilindrada, carga
    vehiculos.append(vehiculo4)
    print(vehiculo4)

    catalogar(vehiculos)






