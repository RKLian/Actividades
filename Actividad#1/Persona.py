class Persona:
    def __init__ (self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def ObtenerNombre(self):
        return F'Mi nombre es {self.nombre} {self.apellido}'