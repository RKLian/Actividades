class Lote:
    def __init__(self, largo, ancho, constructora):
        self.largo = largo
        self.ancho = ancho
        self.constructora = constructora
    def calcularArea(self):
        print(self.largo * self.ancho)
    def NombreConstructora(self):
        print(self.constructora)

class Casa (Lote):
    def __init__(self, largo, ancho, constructora, telefono, propietario):
        super().__init__(largo, ancho, constructora)
        self.telefono = telefono
        self.propietario = propietario
    def NombrePropietario(self):
        print(self.propietario)
    def NumeroTelefono(self):
        print(self.telefono)

x = Casa(7,4,"RKGuild","Yulian Liud Herrera Zuñiga","3157213570")
x.calcularArea()
x.NombreConstructora()
x.NombrePropietario()
x.NumeroTelefono()        