class Mascotas:
    def __init__(self,nombre,raza,color):
        self.nombre=nombre
        self.raza=raza
        self.color=color
punto=Mascotas("nala","esfinge","rosa")
print(type(Mascotas))
print(punto.color)

