class Factura:
    def __init__(self, ID, Vendedor, Fecha_Compra):
        self.ID = ID
        self.Vendedor = Vendedor
        self.Fecha_Compra = Fecha_Compra
    def Imprimir_ID(self):
        print(self.ID)
    def Imprimir_Vendedor(self):
        print(self.Vendedor)
    def Imprimir_FechaCompra(self):
        print(self.Fecha_Compra)

class Detalle_Factura (Factura):
    def __init__(self, ID, Vendedor, Fecha_Compra, Producto, Precio, Cantidad, Total):
        super().__init__(ID, Vendedor, Fecha_Compra)
        self.Producto = Producto
        self.Precio = Precio
        self.Cantidad = Cantidad
        self.Total = Total

    def Imprimir_DetalleFactura(self):
        print(self.Producto)
        print(self.Cantidad)
        print(self.Precio)
    def Total_Factura(self):
        print(self.Precio * self.Cantidad)
        print(self.Total)

x = Detalle_Factura("1042578409", "Yulian", "03/03/2024", "Elemento comprado: Sky - Nintendo Pack", 15000, 10, "Precio total: $150.000")
x.Total_Factura()