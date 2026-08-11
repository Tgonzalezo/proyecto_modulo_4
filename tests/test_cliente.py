import unittest

from modelos.cliente_regular import ClienteRegular
from modelos.cliente_premium import ClientePremium
from modelos.cliente_corporativo import ClienteCorporativo

from excepciones.excepciones import (
    EmailInvalidoError,
    TelefonoInvalidoError
)


class TestCliente(unittest.TestCase):

    def test_crear_cliente_regular(self):

        cliente = ClienteRegular(
            1,
            "Tomas Gonzalez",
            "tomas@gmail.com",
            "912345678",
            "San Miguel"
        )

        self.assertEqual(
            cliente.nombre,
            "Tomas Gonzalez"
        )

        self.assertEqual(
            cliente.email,
            "tomas@gmail.com"
        )

    def test_email_invalido(self):

        with self.assertRaises(
            EmailInvalidoError
        ):

            ClienteRegular(
                1,
                "Tomas Gonzalez",
                "tomasgmail.com",
                "912345678",
                "San Miguel"
            )

    def test_telefono_invalido(self):

        with self.assertRaises(
            TelefonoInvalidoError
        ):

            ClienteRegular(
                1,
                "Tomas Gonzalez",
                "tomas@gmail.com",
                "123",
                "San Miguel"
            )

    def test_beneficio_regular(self):

        cliente = ClienteRegular(
            1,
            "Tomas Gonzalez",
            "tomas@gmail.com",
            "912345678",
            "San Miguel"
        )

        self.assertEqual(
            cliente.obtener_beneficio(),
            "20% de descuento"
        )

    def test_beneficio_premium(self):

        cliente = ClientePremium(
            2,
            "Myriam Orellana",
            "myriam@gmail.com",
            "923456789",
            "San Bernardo"
        )

        self.assertEqual(
            cliente.obtener_beneficio(),
            "Atención personalizada y 30% de descuento"
        )

    def test_beneficio_corporativo(self):

        cliente = ClienteCorporativo(
            3,
            "Cesar Gonzalez",
            "cesar@gmail.com",
            "934567890",
            "San Bernardo"
        )

        self.assertEqual(
            cliente.obtener_beneficio(),
            "40% de descuento y atención personalizada"
        )


if __name__ == "__main__":
    unittest.main()