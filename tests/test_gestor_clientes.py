import unittest

from modelos.cliente_regular import ClienteRegular

from servicios.gestor_clientes import GestorClientes

from excepciones.excepciones import ClienteDuplicadoError


class TestGestorClientes(unittest.TestCase):

    def setUp(self):

        self.gestor = GestorClientes()

        self.cliente = ClienteRegular(
            1,
            "Tomas Gonzalez",
            "tomas@gmail.com",
            "912345678",
            "San Miguel"
        )

    def test_agregar_cliente(self):

        self.gestor.agregar_cliente(
            self.cliente
        )

        self.assertEqual(
            len(self.gestor.clientes),
            1
        )

    def test_buscar_cliente(self):

        self.gestor.agregar_cliente(
            self.cliente
        )

        cliente_encontrado = (
            self.gestor.buscar_cliente(1)
        )

        self.assertEqual(
            cliente_encontrado.nombre,
            "Tomas Gonzalez"
        )

    def test_eliminar_cliente(self):

        self.gestor.agregar_cliente(
            self.cliente
        )

        self.gestor.eliminar_cliente(1)

        self.assertEqual(
            len(self.gestor.clientes),
            0
        )

    def test_cliente_duplicado(self):

        self.gestor.agregar_cliente(
            self.cliente
        )

        cliente_repetido = ClienteRegular(
            1,
            "Pedro Soto",
            "pedro@gmail.com",
            "945678123",
            "Maipú"
        )

        with self.assertRaises(
            ClienteDuplicadoError
        ):

            self.gestor.agregar_cliente(
                cliente_repetido
            )

    def test_editar_cliente(self):

        self.gestor.agregar_cliente(
            self.cliente
        )

        self.gestor.editar_cliente(
            1,
            "Tomas Gonzalez",
            "tomas.nuevo@gmail.com",
            "912345678",
            "Providencia"
        )

        cliente_editado = (
            self.gestor.buscar_cliente(1)
        )

        self.assertEqual(
            cliente_editado.email,
            "tomas.nuevo@gmail.com"
        )

        self.assertEqual(
            cliente_editado.direccion,
            "Providencia"
        )


if __name__ == "__main__":
    unittest.main()