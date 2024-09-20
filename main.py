
from subclase.coche import Coche
from subclase.bicicleta import Bicicleta
from subsubclase.motocicleta import Motocicleta
from subsubclase.camioneta import Camioneta

if __name__ == "__main__":
    vehiculos = []

    vehiculo1 = Coche("Blanco", 4, 150, 1800)
    vehiculos.append(vehiculo1)
    print(vehiculo1)

    vehiculo2 = Bicicleta("Azul", 2, "Urbana")
    vehiculos.append(vehiculo2)
    print(vehiculo2)

    vehiculo3 = Motocicleta("Negra", 2, "Deportiva", 180, 900)
    vehiculos.append(vehiculo3)
    print(vehiculo3)

    vehiculo4 = Camioneta("Gris", 4, 100, 2200, 1500)
    vehiculos.append(vehiculo4)
    print(vehiculo4)

    

