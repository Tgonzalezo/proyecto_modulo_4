from modelos.cliente import Cliente
class ClienteCorporativo(Cliente):
    def __init__(self, id_cliente, nombre, email, telefono, direccion):
        super().__init__(id_cliente, nombre, email, telefono, direccion)
    def obtener_beneficio(self):
        return "40% de descuento y atención personalizada"