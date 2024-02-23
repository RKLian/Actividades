class Estudiante:
    def __init__ (self, nombre, apellido, cedula, correo, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.correo = correo
        self.telefono = telefono

    def ObtenerNombre(self):
        return F'{self.nombre} {self.apellido}'
    def ObtenerCeduda(self):
        return F'{self.cedula}'
    def ObtenerCorreo(self):
        return F'{self.correo}'
    def ObtenerTelefono(self):
        return F'{self.telefono}'
    
P = Estudiante ("Yulian", "Herrera", "1042578409", "yulianhz2004@gmail.com", "+573157213570")
print ("Mi nombre es", P.ObtenerNombre(), "de identificación", P.ObtenerCeduda(), "mi correo es", P.ObtenerCorreo(), "y mi telefono es", P.ObtenerTelefono())