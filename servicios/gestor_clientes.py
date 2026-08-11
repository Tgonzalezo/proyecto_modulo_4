from excepciones.excepciones import ClienteDuplicadoError


class GestorClientes:

    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, cliente):

        if self.buscar_cliente(cliente.id_cliente):
            raise ClienteDuplicadoError(
                f"Ya existe un cliente con el ID {cliente.id_cliente}."
            )

        self.clientes.append(cliente)
        print("Cliente agregado correctamente.")

    def listar_clientes(self):

        if not self.clientes:
            print("No hay clientes registrados.")
            return

        print("\n=== LISTA DE CLIENTES ===")

        for cliente in self.clientes:
            print(cliente)

    def buscar_cliente(self, id_cliente):

        for cliente in self.clientes:

            if cliente.id_cliente == id_cliente:
                return cliente

        return None

    def editar_cliente(
        self,
        id_cliente,
        nombre,
        email,
        telefono,
        direccion
    ):

        cliente = self.buscar_cliente(id_cliente)

        if cliente is None:
            print("Cliente no encontrado.")
            return

        cliente.nombre = nombre
        cliente.email = email
        cliente.telefono = telefono
        cliente.direccion = direccion

        print("Cliente actualizado correctamente.")

    def eliminar_cliente(self, id_cliente):

        cliente = self.buscar_cliente(id_cliente)

        if cliente is not None:
            self.clientes.remove(cliente)
            print("Cliente eliminado correctamente.")
        else:
            print("Cliente no encontrado.")