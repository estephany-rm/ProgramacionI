# Estephany Ruales

import json

# =========================================================================
# Ejercicio 1
# =========================================================================
def calcular_promedio(numeros):
    """Calcula el promedio de una lista de números.
    Maneja ZeroDivisionError y TypeError explícitamente.
    """
    try:
        total = sum(numeros)
        promedio = total / len(numeros)
        return promedio
    except ZeroDivisionError as e:
        print("Error: la lista está vacía. No se puede calcular el promedio.")
        return None
    except TypeError as e:
        print("Error: la lista contiene elementos no numéricos:", e)
        return None


# =========================================================================
# Ejercicio 2
# =========================================================================
def guardar_datos(datos, archivo):
    """Guarda datos en un archivo. Devuelve True si tuvo éxito, False si no.
    Proporciona retroalimentación al usuario mediante prints y captura
    excepciones de I/O y de tipo.
    """
    try:
        with open(archivo, 'w', encoding='utf-8') as f:
            f.write(str(datos))
        print(f"Datos guardados correctamente en '{archivo}'.")
        return True
    except FileNotFoundError:
        print(f"Error: ruta no encontrada: '{archivo}'.")
        return False
    except PermissionError:
        print(f"Error: permiso denegado al escribir en '{archivo}'.")
        return False
    except Exception as e:
        print("Ocurrió un error inesperado al guardar los datos:", e)
        return False


# =========================================================================
# Ejercicio 3
# =========================================================================
def procesar_archivo(nombre_archivo):
    """Lee y procesa un archivo usando try-except-else-finally.
    Retorna un diccionario con conteos si tiene éxito, o None si falla.
    """
    f = None
    try:
        f = open(nombre_archivo, 'r', encoding='utf-8')
        contenido = f.read()
    except FileNotFoundError:
        print(f"Error: archivo '{nombre_archivo}' no encontrado.")
        return None
    except Exception as e:
        print(f"Error al leer '{nombre_archivo}':", e)
        return None
    else:
        # Procesamiento sencillo: conteo de líneas, palabras y caracteres
        lineas = contenido.splitlines()
        palabras = contenido.split()
        resultado = {
            "lineas": len(lineas),
            "palabras": len(palabras),
            "caracteres": len(contenido)
        }
        print(f"Archivo '{nombre_archivo}' procesado correctamente:", resultado)
        return resultado
    finally:
        if f is not None:
            try:
                f.close()
            except Exception:
                pass


# =========================================================================
# Ejercicio 4
# =========================================================================
def crear_usuario(nombre_usuario, edad, email):
    """Crea un nuevo usuario tras validar los parámetros.

    - nombre_usuario: al menos 3 caracteres -> ValueError
    - edad: debe ser int -> TypeError
    - edad: 0 <= edad <= 150 -> ValueError
    - email: debe contener '@' -> ValueError
    Retorna un dict con la info si es válido.
    """
    if not isinstance(nombre_usuario, str):
        raise TypeError("nombre_usuario debe ser una cadena de texto")
    if len(nombre_usuario) < 3:
        raise ValueError("nombre_usuario debe tener al menos 3 caracteres")
    if not isinstance(edad, int):
        raise TypeError("edad debe ser un entero")
    if edad < 0 or edad > 150:
        raise ValueError("edad debe estar entre 0 y 150")
    if not isinstance(email, str) or "@" not in email:
        raise ValueError("email inválido: debe contener '@'")
    usuario = {"nombre": nombre_usuario, "edad": edad, "email": email}
    print("Usuario creado:", usuario)
    return usuario


# =========================================================================
# Ejercicio 5
# =========================================================================
class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, monto):
        self.saldo = saldo
        self.monto = monto
        super().__init__(f"Saldo insuficiente: necesitas ${monto}, tienes ${saldo}")


class MontoInvalidoError(Exception):
    pass


def retirar(saldo, monto):
    """Retira dinero de una cuenta, validando monto y saldo."""
    if monto <= 0:
        raise MontoInvalidoError("El monto debe ser mayor que 0")
    if monto > saldo:
        raise SaldoInsuficienteError(saldo, monto)
    nuevo_saldo = saldo - monto
    print(f"Retiro exitoso. Nuevo saldo: {nuevo_saldo}")
    return nuevo_saldo


# =========================================================================
# Ejercicio 6
# =========================================================================
def procesar_lista_numeros(lista_strings):
    """Convierte strings a int, los duplica y guarda errores.

    Retorna (resultados_exitosos, lista_errores) donde lista_errores es
    una lista de tuples: (valor_original, excepcion_str)
    """
    exitosos = []
    errores = []
    for item in lista_strings:
        try:
            n = int(item)
            exitosos.append(n * 2)
        except Exception as e:
            errores.append((item, repr(e)))
            # continue con los demás elementos
    return exitosos, errores


# =========================================================================
# Ejercicio 7
# =========================================================================
def operacion_critica(valor):
    """Realiza una operación crítica. Registro y re-lanzamiento de errores."""
    try:
        resultado = 100 / int(valor)
        return resultado
    except (ValueError, ZeroDivisionError) as e:
        print(f"[operacion_critica] Error al procesar valor={valor}: {e}")
        raise


# =========================================================================
# Ejercicio 8
# =========================================================================
def calculadora_segura(operacion, a, b):
    """Calculadora que maneja varios tipos de excepción de forma separada."""
    try:
        if operacion == "suma":
            return a + b
        elif operacion == "resta":
            return a - b
        elif operacion in ("multiplicacion", "multiplica", "multiplicar"):
            return a * b
        elif operacion in ("division", "divide", "dividir"):
            return a / b
        else:
            raise ValueError(f"Operación inválida: {operacion}")
    except ZeroDivisionError:
        return "Error: división por cero."
    except TypeError:
        return "Error: tipos de operandos incorrectos."
    except ValueError as e:
        return f"Error: {e}"


# =========================================================================
# Ejercicio 9
# =========================================================================
def parsear_configuracion(json_string):
    """Parsea JSON y preserva el contexto en caso de error."""
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        raise ValueError("JSON inválido en configuración") from e


# =========================================================================
# Ejercicio 10 - Inventario
# =========================================================================
class ErrorInventario(Exception):
    pass


class ProductoNoEncontrado(ErrorInventario):
    pass


class StockInsuficiente(ErrorInventario):
    pass


class Inventario:
    """Sistema de inventario con manejo de excepciones personalizado."""

    def __init__(self):
        self.productos = {}  # codigo -> {"nombre": ..., "cantidad": ...}

    def agregar_producto(self, codigo, nombre, cantidad):
        if not isinstance(cantidad, int):
            raise TypeError("cantidad debe ser un entero")
        if cantidad <= 0:
            raise ValueError("cantidad debe ser mayor que 0")
        if codigo in self.productos:
            raise KeyError(f"El código '{codigo}' ya existe en el inventario")
        self.productos[codigo] = {"nombre": nombre, "cantidad": cantidad}
        print(f"Producto agregado: {codigo} -> {self.productos[codigo]}")

    def retirar_stock(self, codigo, cantidad):
        if codigo not in self.productos:
            raise ProductoNoEncontrado(f"Producto con código '{codigo}' no encontrado")
        if not isinstance(cantidad, int):
            raise TypeError("cantidad debe ser un entero")
        if cantidad <= 0:
            raise ValueError("cantidad debe ser mayor que 0")
        existente = self.productos[codigo]["cantidad"]
        if cantidad > existente:
            raise StockInsuficiente(f"Stock insuficiente: solicitado={cantidad}, disponible={existente}")
        self.productos[codigo]["cantidad"] = existente - cantidad
        print(f"Retiro realizado. Nuevo stock de {codigo}: {self.productos[codigo]['cantidad']}")
        return self.productos[codigo]["cantidad"]

    def obtener_producto(self, codigo):
        if codigo not in self.productos:
            raise ProductoNoEncontrado(f"Producto con código '{codigo}' no encontrado")
        return self.productos[codigo]


# =========================================================================
# Bloque de pruebas básicas (se ejecuta si se corre el archivo directamente)
# =========================================================================
if __name__ == "__main__":
    print("\n--- Pruebas rápidas de funciones implementadas ---\n")

    # Ejercicio 1: pruebas con prints
    print("promedio [1..5]:", calcular_promedio([1, 2, 3, 4, 5]))  # Debería funcionar
    print("promedio []:", calcular_promedio([]))  # Debería manejar lista vacía
    print("promedio con tipo inválido:", calcular_promedio([1, 2, 'a']))  # Debería manejar error de tipo

    # Ejercicio 2
    guardar_datos({"usuario": "Ana"}, "datos_prueba.txt")
    guardar_datos({"usuario": "Ana"}, "ruta_invalida/datos.txt")  # debería fallar

    # Ejercicio 3
    ejemplo = "archivo_ejemplo.txt"
    with open(ejemplo, 'w', encoding='utf-8') as f:
        f.write("Linea1\nLinea2\nPalabras aqui\n")
    procesar_archivo(ejemplo)
    procesar_archivo("no_existe_este_archivo.txt")  # debería informar error

    # Ejercicio 4
    try:
        crear_usuario("Ana", 25, "ana@example.com")
    except Exception as e:
        print("Error creando usuario:", e)
    try:
        crear_usuario("Ab", 25, "ana@example.com")
    except Exception as e:
        print("Error (esperado):", e)

    # Ejercicio 5
    try:
        print("Retirar 50 de 100 ->", retirar(100, 50))
    except Exception as e:
        print("Error retirando:", e)
    try:
        retirar(100, 150)
    except Exception as e:
        print("Error (esperado):", e)
    try:
        retirar(100, -10)
    except Exception as e:
        print("Error (esperado):", e)

    # Ejercicio 6
    res, errs = procesar_lista_numeros(["1", "2", "abc", "4", "xyz"])
    print("Exitosos:", res)
    print("Errores:", errs)

    # Ejercicio 7
    try:
        print("operacion_critica('10') ->", operacion_critica("10"))
        operacion_critica("0")  # re-lanzará ZeroDivisionError
    except Exception as e:
        print("Llamador: capturado ->", type(e).__name__, e)

    # Ejercicio 8
    print("suma:", calculadora_segura("suma", 10, 5))
    print("division por cero:", calculadora_segura("division", 10, 0))
    print("tipo inválido:", calculadora_segura("suma", 10, "5"))
    print("operacion inválida:", calculadora_segura("potencia", 2, 3))

    # Ejercicio 9
    try:
        print(parsear_configuracion('{"nombre": "Ana"}'))
    except Exception as e:
        print("Error parseando (no debería):", e)
    try:
        parsear_configuracion('json invalido')
    except Exception as e:
        print("Error esperado al parsear JSON inválido:", e)
        if getattr(e, '__cause__', None):
            print("Causa original:", type(e.__cause__).__name__, e.__cause__)

    # Ejercicio 10
    inv = Inventario()
    try:
        inv.agregar_producto("001", "Laptop", 10)
        print(inv.obtener_producto("001"))
        inv.retirar_stock("001", 5)
        try:
            inv.retirar_stock("001", 10)  # debería lanzar StockInsuficiente
        except Exception as e:
            print("Error esperado:", e)
    except Exception as e:
        print("Error en inventario:", e)

    print("¿Completado? [Sí/No]: SI")