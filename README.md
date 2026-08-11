# Gestor Inteligente de Clientes

Proyecto desarrollado en Python para la gestión de clientes de la empresa ficticia SolutionTech.

El sistema permite registrar, visualizar, buscar, editar y eliminar clientes, diferenciándolos según su tipo: Regular, Premium o Corporativo.

Además, incorpora validaciones de datos, manejo de excepciones, persistencia en archivos JSON, exportación a CSV, interfaz gráfica con Tkinter, registro de errores y pruebas unitarias.

---

## Funcionalidades principales

- Registrar clientes.
- Listar clientes registrados.
- Buscar clientes por ID.
- Editar información de clientes.
- Eliminar clientes.
- Diferenciar clientes por tipo:
  - Cliente Regular.
  - Cliente Premium.
  - Cliente Corporativo.
- Asignar beneficios según el tipo de cliente.
- Validar email y teléfono.
- Detectar clientes duplicados.
- Guardar y cargar clientes desde JSON.
- Exportar clientes a CSV.
- Registrar errores en archivos de log.
- Gestionar clientes mediante una interfaz gráfica desarrollada con Tkinter.

---

## Tipos de clientes

### Cliente Regular

Beneficio:

- 20% de descuento.

### Cliente Premium

Beneficios:

- Atención personalizada.
- 30% de descuento.

### Cliente Corporativo

Beneficios:

- Atención personalizada.
- 40% de descuento.

---

## Programación Orientada a Objetos

El proyecto aplica distintos conceptos de Programación Orientada a Objetos.

### Clase padre

La clase `Cliente` contiene los atributos y métodos comunes de todos los clientes.

Atributos principales:

- ID del cliente.
- Nombre.
- Email.
- Teléfono.
- Dirección.

### Herencia

Las siguientes clases heredan de `Cliente`:

- `ClienteRegular`
- `ClientePremium`
- `ClienteCorporativo`

### Polimorfismo

Cada tipo de cliente implementa el método:

`obtener_beneficio()`

El comportamiento del método cambia según el tipo de cliente.

### Encapsulación

Los atributos de email y teléfono utilizan propiedades para controlar el acceso y realizar validaciones antes de almacenar los datos.

### Métodos especiales

La clase `Cliente` incorpora:

- `__str__()`
- `__eq__()`

Estos métodos permiten representar objetos como texto y comparar clientes.

---

## Validaciones

El sistema incorpora validaciones para evitar el ingreso de información incorrecta.

### Email

El email debe contener una estructura válida.

Ejemplo:

`cliente@gmail.com`

### Teléfono

El teléfono:

- Debe contener solamente números.
- Debe tener 9 dígitos.

---

## Manejo de excepciones

El proyecto utiliza excepciones personalizadas:

- `EmailInvalidoError`
- `TelefonoInvalidoError`
- `ClienteDuplicadoError`

Estas permiten controlar errores específicos del sistema.

Los errores también son registrados mediante el módulo `logging`.

El archivo de registro se encuentra en:

`logs/errores.log`

---

## Persistencia de datos

### JSON

Los clientes se guardan automáticamente en:

`datos/clientes.json`

Al iniciar el programa, los clientes guardados anteriormente son cargados nuevamente.

### CSV

El sistema permite exportar los clientes a:

`datos/clientes.csv`

El archivo incluye:

- ID.
- Nombre.
- Email.
- Teléfono.
- Dirección.
- Tipo de cliente.
- Beneficio.

---

## Interfaz gráfica

La interfaz gráfica fue desarrollada utilizando Tkinter.

Permite:

- Registrar clientes.
- Visualizar clientes en una tabla.
- Seleccionar clientes.
- Editar clientes.
- Eliminar clientes.
- Exportar información a CSV.
- Limpiar los campos del formulario.

---

## Estructura del proyecto

```text
gestor_clientes/
│
├── main.py
├── README.md
│
├── datos/
│   ├── clientes.json
│   └── clientes.csv
│
├── excepciones/
│   ├── __init__.py
│   └── excepciones.py
│
├── interfaz/
│   ├── __init__.py
│   └── ventana.py
│
├── logs/
│   └── errores.log
│
├── modelos/
│   ├── __init__.py
│   ├── cliente.py
│   ├── cliente_regular.py
│   ├── cliente_premium.py
│   └── cliente_corporativo.py
│
├── servicios/
│   ├── __init__.py
│   ├── gestor_clientes.py
│   ├── archivo_json.py
│   ├── archivo_csv.py
│   └── logger.py
│
└── tests/
    ├── __init__.py
    ├── test_cliente.py
    └── test_gestor_clientes.py

## Autor

Tamara González Orellana

Proyecto desarrollado como evaluación del módulo 4