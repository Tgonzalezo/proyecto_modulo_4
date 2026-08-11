from modelos.cliente import Cliente
class ClienteRegular(Cliente):
    def __init__(self, id_cliente, nombre, email, telefono, direccion):
        super().__init__(id_cliente, nombre, email, telefono, direccion)
    def obtener_beneficio(self):
        return "20% de descuento"

