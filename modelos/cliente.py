from excepciones.excepciones import EmailInvalidoError, TelefonoInvalidoError

class Cliente:

    def __init__(self, id_cliente, nombre, email, telefono, direccion):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.direccion = direccion

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, nuevo_email):
        if "@" not in nuevo_email or "." not in nuevo_email:
            raise EmailInvalidoError("El email ingresado no es válido.")

        self._email = nuevo_email

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, nuevo_telefono):
        if not nuevo_telefono.isdigit():
            raise TelefonoInvalidoError(
                "El teléfono debe contener solo números."
            )

        if len(nuevo_telefono) != 9:
            raise TelefonoInvalidoError(
                "El teléfono debe tener 9 dígitos."
            )

        self._telefono = nuevo_telefono

    def mostrar_informacion(self):
        print(f"ID: {self.id_cliente}")
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Teléfono: {self.telefono}")
        print(f"Dirección: {self.direccion}")

    def __str__(self):
        return (
            f"Cliente: {self.nombre} | "
            f"Email: {self.email} | "
            f"Teléfono: {self.telefono}"
        )

    def __eq__(self, otro):
        if isinstance(otro, Cliente):
            return self.id_cliente == otro.id_cliente

        return False