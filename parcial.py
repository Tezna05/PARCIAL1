#EJEMPLO 1
class Vehiculos:
    def __init__(self,color, marca,velocidad):
        self.color=color
        self.marca=marca
        self.velocidad=velocidad
fiesta=Vehiculos("rojo","ford",149)
fiesta2=Vehiculos("azul","tesla",322)
print(type(fiesta))
print(fiesta.marca)
print(fiesta2.velocidad)