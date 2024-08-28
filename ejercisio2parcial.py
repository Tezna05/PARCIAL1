class vegetal:
    def __init__(self,color,sabor,nombre):
        self.color=color
        self.sabor=sabor
        self.nombre=nombre
vegetal1=vegetal("rojo","agrio","limon")
print(type(vegetal1))
print(vegetal1.sabor)