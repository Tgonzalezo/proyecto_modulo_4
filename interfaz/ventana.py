import tkinter as tk
from tkinter import ttk, messagebox

from modelos.cliente_regular import ClienteRegular
from modelos.cliente_premium import ClientePremium
from modelos.cliente_corporativo import ClienteCorporativo

from servicios.gestor_clientes import GestorClientes
from servicios.archivo_json import guardar_clientes, cargar_clientes
from servicios.archivo_csv import exportar_clientes_csv
from servicios.logger import registrar_error

from excepciones.excepciones import (
    EmailInvalidoError,
    TelefonoInvalidoError,
    ClienteDuplicadoError
)


class VentanaPrincipal:

    def __init__(self, root):
        self.root = root

        self.root.title("Gestor de Clientes")
        self.root.geometry("1000x700")

        self.gestor = GestorClientes()

        try:
            self.gestor.clientes = cargar_clientes()

        except Exception as error:
            registrar_error(
                f"Error al cargar clientes desde JSON: {error}"
            )

            self.gestor.clientes = []

        titulo = tk.Label(
            self.root,
            text="Gestor Inteligente de Clientes",
            font=("Arial", 18, "bold")
        )

        titulo.pack(pady=15)

        # =========================
        # FORMULARIO
        # =========================

        frame_formulario = tk.Frame(self.root)
        frame_formulario.pack(pady=10)

        tk.Label(
            frame_formulario,
            text="ID Cliente:"
        ).grid(row=0, column=0, padx=10, pady=5)

        self.entrada_id = tk.Entry(frame_formulario)
        self.entrada_id.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(
            frame_formulario,
            text="Nombre:"
        ).grid(row=1, column=0, padx=10, pady=5)

        self.entrada_nombre = tk.Entry(frame_formulario)
        self.entrada_nombre.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(
            frame_formulario,
            text="Email:"
        ).grid(row=2, column=0, padx=10, pady=5)

        self.entrada_email = tk.Entry(frame_formulario)
        self.entrada_email.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(
            frame_formulario,
            text="Teléfono:"
        ).grid(row=3, column=0, padx=10, pady=5)

        self.entrada_telefono = tk.Entry(frame_formulario)
        self.entrada_telefono.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(
            frame_formulario,
            text="Dirección:"
        ).grid(row=4, column=0, padx=10, pady=5)

        self.entrada_direccion = tk.Entry(frame_formulario)
        self.entrada_direccion.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(
            frame_formulario,
            text="Tipo de cliente:"
        ).grid(row=5, column=0, padx=10, pady=5)

        self.combo_tipo = ttk.Combobox(
            frame_formulario,
            values=[
                "Regular",
                "Premium",
                "Corporativo"
            ],
            state="readonly"
        )

        self.combo_tipo.grid(
            row=5,
            column=1,
            padx=10,
            pady=5
        )

        self.combo_tipo.current(0)

        # =========================
        # BOTONES
        # =========================

        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        boton_registrar = tk.Button(
            frame_botones,
            text="Registrar cliente",
            command=self.registrar_cliente
        )

        boton_registrar.grid(
            row=0,
            column=0,
            padx=8
        )

        boton_editar = tk.Button(
            frame_botones,
            text="Editar cliente",
            command=self.editar_cliente
        )

        boton_editar.grid(
            row=0,
            column=1,
            padx=8
        )

        boton_eliminar = tk.Button(
            frame_botones,
            text="Eliminar cliente",
            command=self.eliminar_cliente
        )

        boton_eliminar.grid(
            row=0,
            column=2,
            padx=8
        )

        boton_exportar = tk.Button(
            frame_botones,
            text="Exportar a CSV",
            command=self.exportar_csv
        )

        boton_exportar.grid(
            row=0,
            column=3,
            padx=8
        )

        boton_limpiar = tk.Button(
            frame_botones,
            text="Limpiar campos",
            command=self.limpiar_campos
        )

        boton_limpiar.grid(
            row=0,
            column=4,
            padx=8
        )

        # =========================
        # TABLA
        # =========================

        frame_tabla = tk.Frame(self.root)

        frame_tabla.pack(
            pady=15,
            padx=20,
            fill="both",
            expand=True
        )

        columnas = (
            "id",
            "nombre",
            "email",
            "telefono",
            "direccion",
            "tipo",
            "beneficio"
        )

        self.tabla_clientes = ttk.Treeview(
            frame_tabla,
            columns=columnas,
            show="headings"
        )

        self.tabla_clientes.heading(
            "id",
            text="ID"
        )

        self.tabla_clientes.heading(
            "nombre",
            text="Nombre"
        )

        self.tabla_clientes.heading(
            "email",
            text="Email"
        )

        self.tabla_clientes.heading(
            "telefono",
            text="Teléfono"
        )

        self.tabla_clientes.heading(
            "direccion",
            text="Dirección"
        )

        self.tabla_clientes.heading(
            "tipo",
            text="Tipo"
        )

        self.tabla_clientes.heading(
            "beneficio",
            text="Beneficio"
        )

        self.tabla_clientes.column(
            "id",
            width=50
        )

        self.tabla_clientes.column(
            "nombre",
            width=140
        )

        self.tabla_clientes.column(
            "email",
            width=170
        )

        self.tabla_clientes.column(
            "telefono",
            width=100
        )

        self.tabla_clientes.column(
            "direccion",
            width=120
        )

        self.tabla_clientes.column(
            "tipo",
            width=110
        )

        self.tabla_clientes.column(
            "beneficio",
            width=220
        )

        self.tabla_clientes.pack(
            fill="both",
            expand=True
        )

        self.tabla_clientes.bind(
            "<<TreeviewSelect>>",
            self.cargar_cliente_seleccionado
        )

        self.actualizar_tabla()

    # =========================
    # REGISTRAR CLIENTE
    # =========================

    def registrar_cliente(self):

        try:
            id_cliente = int(
                self.entrada_id.get()
            )

            nombre = self.entrada_nombre.get()
            email = self.entrada_email.get()
            telefono = self.entrada_telefono.get()
            direccion = self.entrada_direccion.get()

            tipo = self.combo_tipo.get()

            if tipo == "Regular":

                cliente = ClienteRegular(
                    id_cliente,
                    nombre,
                    email,
                    telefono,
                    direccion
                )

            elif tipo == "Premium":

                cliente = ClientePremium(
                    id_cliente,
                    nombre,
                    email,
                    telefono,
                    direccion
                )

            elif tipo == "Corporativo":

                cliente = ClienteCorporativo(
                    id_cliente,
                    nombre,
                    email,
                    telefono,
                    direccion
                )

            else:

                messagebox.showerror(
                    "Error",
                    "Seleccione un tipo de cliente."
                )

                return

            self.gestor.agregar_cliente(
                cliente
            )

            guardar_clientes(
                self.gestor.clientes
            )

            self.actualizar_tabla()

            messagebox.showinfo(
                "Registro exitoso",
                "Cliente registrado correctamente."
            )

            self.limpiar_campos()

        except ValueError as error:

            registrar_error(
                f"ID inválido al registrar cliente: {error}"
            )

            messagebox.showerror(
                "Error",
                "El ID debe ser un número."
            )

        except EmailInvalidoError as error:

            registrar_error(
                f"Email inválido: {error}"
            )

            messagebox.showerror(
                "Error de email",
                str(error)
            )

        except TelefonoInvalidoError as error:

            registrar_error(
                f"Teléfono inválido: {error}"
            )

            messagebox.showerror(
                "Error de teléfono",
                str(error)
            )

        except ClienteDuplicadoError as error:

            registrar_error(
                f"Cliente duplicado: {error}"
            )

            messagebox.showerror(
                "Cliente duplicado",
                str(error)
            )

        except Exception as error:

            registrar_error(
                f"Error inesperado al registrar cliente: {error}"
            )

            messagebox.showerror(
                "Error",
                "Ocurrió un error inesperado."
            )

    # =========================
    # CARGAR CLIENTE SELECCIONADO
    # =========================

    def cargar_cliente_seleccionado(
        self,
        event
    ):

        seleccion = (
            self.tabla_clientes.selection()
        )

        if not seleccion:
            return

        fila = self.tabla_clientes.item(
            seleccion[0]
        )

        valores = fila["values"]

        self.limpiar_campos()

        self.entrada_id.insert(
            0,
            valores[0]
        )

        self.entrada_nombre.insert(
            0,
            valores[1]
        )

        self.entrada_email.insert(
            0,
            valores[2]
        )

        self.entrada_telefono.insert(
            0,
            valores[3]
        )

        self.entrada_direccion.insert(
            0,
            valores[4]
        )

        tipo = valores[5]

        if tipo == "ClienteRegular":
            self.combo_tipo.set(
                "Regular"
            )

        elif tipo == "ClientePremium":
            self.combo_tipo.set(
                "Premium"
            )

        elif tipo == "ClienteCorporativo":
            self.combo_tipo.set(
                "Corporativo"
            )

    # =========================
    # EDITAR CLIENTE
    # =========================

    def editar_cliente(self):

        try:
            id_cliente = int(
                self.entrada_id.get()
            )

            cliente = (
                self.gestor.buscar_cliente(
                    id_cliente
                )
            )

            if cliente is None:

                messagebox.showerror(
                    "Error",
                    "Cliente no encontrado."
                )

                return

            nombre = self.entrada_nombre.get()
            email = self.entrada_email.get()
            telefono = self.entrada_telefono.get()
            direccion = self.entrada_direccion.get()

            self.gestor.editar_cliente(
                id_cliente,
                nombre,
                email,
                telefono,
                direccion
            )

            guardar_clientes(
                self.gestor.clientes
            )

            self.actualizar_tabla()

            self.limpiar_campos()

            messagebox.showinfo(
                "Edición exitosa",
                "Cliente actualizado correctamente."
            )

        except ValueError as error:

            registrar_error(
                f"ID inválido al editar cliente: {error}"
            )

            messagebox.showerror(
                "Error",
                "Seleccione un cliente válido."
            )

        except EmailInvalidoError as error:

            registrar_error(
                f"Email inválido al editar cliente: {error}"
            )

            messagebox.showerror(
                "Error de email",
                str(error)
            )

        except TelefonoInvalidoError as error:

            registrar_error(
                f"Teléfono inválido al editar cliente: {error}"
            )

            messagebox.showerror(
                "Error de teléfono",
                str(error)
            )

        except Exception as error:

            registrar_error(
                f"Error inesperado al editar cliente: {error}"
            )

            messagebox.showerror(
                "Error",
                "Ocurrió un error inesperado."
            )

    # =========================
    # ELIMINAR CLIENTE
    # =========================

    def eliminar_cliente(self):

        try:
            seleccion = (
                self.tabla_clientes.selection()
            )

            if not seleccion:

                messagebox.showwarning(
                    "Aviso",
                    "Seleccione un cliente para eliminar."
                )

                return

            fila = self.tabla_clientes.item(
                seleccion[0]
            )

            id_cliente = int(
                fila["values"][0]
            )

            respuesta = messagebox.askyesno(
                "Confirmar eliminación",
                "¿Desea eliminar este cliente?"
            )

            if respuesta:

                self.gestor.eliminar_cliente(
                    id_cliente
                )

                guardar_clientes(
                    self.gestor.clientes
                )

                self.actualizar_tabla()

                self.limpiar_campos()

                messagebox.showinfo(
                    "Cliente eliminado",
                    "Cliente eliminado correctamente."
                )

        except Exception as error:

            registrar_error(
                f"Error al eliminar cliente: {error}"
            )

            messagebox.showerror(
                "Error",
                "No fue posible eliminar el cliente."
            )

    # =========================
    # EXPORTAR CSV
    # =========================

    def exportar_csv(self):

        if not self.gestor.clientes:

            messagebox.showwarning(
                "Aviso",
                "No hay clientes para exportar."
            )

            return

        try:

            exportar_clientes_csv(
                self.gestor.clientes
            )

            messagebox.showinfo(
                "Exportación exitosa",
                "Clientes exportados correctamente a CSV."
            )

        except Exception as error:

            registrar_error(
                f"Error al exportar clientes a CSV: {error}"
            )

            messagebox.showerror(
                "Error",
                "No fue posible exportar el archivo."
            )

    # =========================
    # ACTUALIZAR TABLA
    # =========================

    def actualizar_tabla(self):

        for fila in (
            self.tabla_clientes.get_children()
        ):

            self.tabla_clientes.delete(
                fila
            )

        for cliente in self.gestor.clientes:

            tipo_cliente = (
                cliente.__class__.__name__
            )

            self.tabla_clientes.insert(
                "",
                tk.END,
                values=(
                    cliente.id_cliente,
                    cliente.nombre,
                    cliente.email,
                    cliente.telefono,
                    cliente.direccion,
                    tipo_cliente,
                    cliente.obtener_beneficio()
                )
            )

    # =========================
    # LIMPIAR CAMPOS
    # =========================

    def limpiar_campos(self):

        self.entrada_id.delete(
            0,
            tk.END
        )

        self.entrada_nombre.delete(
            0,
            tk.END
        )

        self.entrada_email.delete(
            0,
            tk.END
        )

        self.entrada_telefono.delete(
            0,
            tk.END
        )

        self.entrada_direccion.delete(
            0,
            tk.END
        )

        self.combo_tipo.current(0)