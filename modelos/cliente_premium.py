from modelos.cliente import Cliente
class ClientePremium(Cliente):
    def __init__(self, id_cliente, nombre, email, telefono, direccion):
        super().__init__(id_cliente, nombre, email, telefono, direccion)
    def obtener_beneficio(self):
        return "Atención personalizada y 30% de descuento"