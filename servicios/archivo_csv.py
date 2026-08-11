import csv
import os


RUTA_CSV = "datos/clientes.csv"


def exportar_clientes_csv(clientes):

    os.makedirs("datos", exist_ok=True)

    with open(RUTA_CSV, "w", newline="", encoding="utf-8-sig") as archivo:

        campos = [
            "id_cliente",
            "nombre",
            "email",
            "telefono",
            "direccion",
            "tipo_cliente",
            "beneficio"
        ]

        escritor = csv.DictWriter(
            archivo,
            fieldnames=campos
        )

        escritor.writeheader()

        for cliente in clientes:
            escritor.writerow(
                {
                    "id_cliente": cliente.id_cliente,
                    "nombre": cliente.nombre,
                    "email": cliente.email,
                    "telefono": cliente.telefono,
                    "direccion": cliente.direccion,
                    "tipo_cliente": cliente.__class__.__name__,
                    "beneficio": cliente.obtener_beneficio()
                }
            )

    print("Clientes exportados correctamente a CSV.")