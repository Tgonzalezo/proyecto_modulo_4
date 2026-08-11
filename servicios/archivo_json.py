import json
import os

from modelos.cliente_regular import ClienteRegular
from modelos.cliente_premium import ClientePremium
from modelos.cliente_corporativo import ClienteCorporativo

RUTA_ARCHIVO = "datos/clientes.json"

def guardar_clientes(clientes):

    datos = []

    for cliente in clientes:
        datos.append(
            {
                "id_cliente": cliente.id_cliente,
                "nombre": cliente.nombre,
                "email": cliente.email,
                "telefono": cliente.telefono,
                "direccion": cliente.direccion,
                "tipo": cliente.__class__.__name__
            }
        )

    os.makedirs("datos", exist_ok=True)

    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

    print("Clientes guardados correctamente en JSON.")


def cargar_clientes():

    if not os.path.exists(RUTA_ARCHIVO):
        return []

    with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    clientes = []

    for dato in datos:

        if dato["tipo"] == "ClienteRegular":
            cliente = ClienteRegular(
                dato["id_cliente"],
                dato["nombre"],
                dato["email"],
                dato["telefono"],
                dato["direccion"]
            )

        elif dato["tipo"] == "ClientePremium":
            cliente = ClientePremium(
                dato["id_cliente"],
                dato["nombre"],
                dato["email"],
                dato["telefono"],
                dato["direccion"]
            )

        elif dato["tipo"] == "ClienteCorporativo":
            cliente = ClienteCorporativo(
                dato["id_cliente"],
                dato["nombre"],
                dato["email"],
                dato["telefono"],
                dato["direccion"]
            )

        else:
            continue

        clientes.append(cliente)

    return clientes