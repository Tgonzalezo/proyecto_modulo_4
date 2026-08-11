import logging
import os


os.makedirs("logs", exist_ok=True)


logging.basicConfig(
    filename="logs/errores.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


def registrar_error(mensaje):
    logging.error(mensaje)