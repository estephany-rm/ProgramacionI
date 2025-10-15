#!/usr/bin/env python3
"""
EJERCICIOS PARA ESTUDIANTES - SOLUCIONES
Archivo resuelto: ejercicios_estudiante_2_solutions.py
"""

# ===========================================================================
# Ejercicio 1: Encuentra y arregla el except desnudo
# ===========================================================================
print("\n--- EJERCICIO 1: ARREGLA EL EXCEPT DESNUDO ---")

def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.
    Manejo específico de excepciones: ZeroDivisionError y TypeError.
    """
    try:
        total = sum(numeros)
        promedio = total / len(numeros)
        return promedio
    except ZeroDivisionError:
        print("Error: la lista está vacía (division por cero).")
        return None
    except TypeError:
        print("Error: la lista contiene elementos no numéricos.")
        return None

# ===========================================================================
# Ejercicio 2: Añade retroalimentación al usuario
# ===========================================================================
print("\n--- EJERCICIO 2: AÑADE RETROALIMENTACIÓN ---")

def guardar_datos(datos, archivo):
    """
    Guarda datos en un archivo con manejo de excepciones y feedback al usuario.
    Retorna True si se guardó correctamente, False en caso contrario.
    """
    try:
        with open(archivo, 'w', encoding='utf-8') as f:
            f.write(str(datos))
        print(f"Datos guardados correctamente en '{archivo}'.")
        return True
    except OSError as e:
        print(f"Error al guardar datos en '{archivo}': {e}")
        return False

# ===========================================================================
# Ejercicio 3: Usa else y finally correctamente
# ===========================================================================
print("\n--- EJERCICIO 3: USA ELSE Y FINALLY ---")

def procesar_archivo(nombre_archivo):
    """
    Lee y procesa un archivo usando try-except-else-finally.
    - try: abrir y leer archivo
    - except: manejar FileNotFoundError
    - else: procesar los datos (solo si lectura exitosa)
    - finally: asegurar que el archivo se cierre
    Retorna el contenido procesado (por ejemplo, número de líneas) o None si hubo error.
    """
    f = None
    try:
        f = open(nombre_archivo, 'r', encoding='utf-8')
        contenido = f.read()
    except FileNotFoundError:
        print(f"Error: el archivo '{nombre_archivo}' no existe.")
        return None
    else:
        # Ejemplo de procesamiento: contar líneas y palabras
        lineas = contenido.splitlines()
        num_lineas = len(lineas)
        num_palabras = len(contenido.split())
        print(f"Archivo leído correctamente: {num_lineas} líneas, {num_palabras} palabras.")
        return {
            'lineas': num_lineas,
            'palabras': num_palabras,
            'contenido': contenido
        }
    finally:
        if f is not None:
            f.close()
            # Notificar que se cerró el archivo (útil para depuración/educativo)
            # (Si se usara 'with', finally no sería estrictamente necesario.)
            # print(f"Archivo '{nombre_archivo}' cerrado.")

# ===========================================================================
# Ejercicio 4: Lanza excepciones apropiadas
# ===========================================================================
print("\n--- EJERCICIO 4: LANZA EXCEPCIONES ---")

def crear_usuario(nombre_usuario, edad, email):
    """
    Crea un nuevo usuario con validación.
    Lanza:
    - ValueError si nombre_usuario tiene menos de 3 caracteres
    - TypeError si edad no es int
    - ValueError si edad fuera de rango (0-150)
    - ValueError si email no contiene '@'
    Retorna un diccionario con los datos si todo es válido.
    """
    if not isinstance(nombre_usuario, str) or len(nombre_usuario) < 3:
        raise ValueError("El nombre de usuario debe tener al menos 3 caracteres.")
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un entero.")
    if edad < 0 or edad > 150:
        raise ValueError("La edad debe estar entre 0 y 150.")
    if not isinstance(email, str) or '@' not in email:
        raise ValueError("El email debe contener '@'.")
    usuario = {
        'nombre': nombre_usuario,
        'edad': edad,
        'email': email
    }
    print("Usuario creado correctamente.")
    return usuario

# ===========================================================================
# Ejercicio 5: Crea excepciones personalizadas
# ===========================================================================
print("\n--- EJERCICIO 5: EXCEPCIONES PERSONALIZADAS ---")

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, monto):
        self.saldo = saldo
        self.monto = monto
        super().__init__(f"Saldo insuficiente: necesitas ${monto}, tienes ${saldo}")

class MontoInvalidoError(Exception):
    pass

def retirar(saldo, monto):
    """
    Retira dinero de una cuenta.
    - Lanza MontoInvalidoError si monto <= 0
    - Lanza SaldoInsuficienteError si monto > saldo
    - Retorna nuevo saldo si exitoso
    """
    if monto <= 0:
        raise MontoInvalidoError("El monto a retirar debe ser mayor que 0.")
    if monto > saldo:
        raise SaldoInsuficienteError(saldo, monto)
    nuevo_saldo = saldo - monto
    print(f"Retiro exitoso. Nuevo saldo: {nuevo_saldo}")
    return nuevo_saldo

# ===========================================================================
# Ejercicio 6: Maneja excepciones en bucles
# ===========================================================================
print("\n--- EJERCICIO 6: EXCEPCIONES EN BUCLES ---")

def procesar_lista_numeros(lista_strings):
    """
    Convierte strings a números y los duplica.
    - Intenta convertir cada elemento a int
    - Si falla, registra el error pero continúa con los demás
    - Retorna tupla (resultados_exitosos, lista_errores)
    """
    exitosos = []
    errores = []
    for elemento in lista_strings:
        try:
            n = int(elemento)
            exitosos.append(n * 2)
        except ValueError as e:
            errores.append((elemento, str(e)))
    return exitosos, errores

# ===========================================================================
# Ejercicio 7: Re-lanza excepciones apropiadamente
# ===========================================================================
print("\n--- EJERCICIO 7: RE-LANZA EXCEPCIONES ---")

def operacion_critica(valor):
    """
    Realiza operación crítica con logging.
    - Si ocurre ValueError o ZeroDivisionError se registra y se relanza.
    """
    try:
        resultado = 100 / int(valor)
        return resultado
    except (ValueError, ZeroDivisionError) as e:
        print(f"[ERROR] en operacion_critica con valor={valor}: {e}")
        raise

# ===========================================================================
# Ejercicio 8: Excepción con múltiples except
# ===========================================================================
print("\n--- EJERCICIO 8: MÚLTIPLES EXCEPT ---")

def calculadora_segura(operacion, a, b):
    """
    Realiza operaciones matemáticas con manejo de errores.
    - ZeroDivisionError: retorna mensaje específico
    - TypeError: retorna mensaje específico
    - ValueError: retorna mensaje específico
    """
    try:
        if operacion == "suma":
            return a + b
        elif operacion == "resta":
            return a - b
        elif operacion == "multiplicacion":
            return a * b
        elif operacion == "division":
            return a / b
        else:
            raise ValueError("Operación no soportada.")
    except ZeroDivisionError:
        return "Error: división por cero."
    except TypeError:
        return "Error: tipos inválidos para la operación."
    except ValueError as e:
        return f"Error: {e}"

# ===========================================================================
# Ejercicio 9: Contexto de excepción
# ===========================================================================
print("\n--- EJERCICIO 9: CONTEXTO DE EXCEPCIÓN ---")

def parsear_configuracion(json_string):
    """
    Parsea configuración JSON y preserva el contexto usando 'from'.
    """
    import json
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        raise ValueError("JSON inválido") from e

# ===========================================================================
# Ejercicio 10: Proyecto completo
# ===========================================================================
print("\n--- EJERCICIO 10: PROYECTO COMPLETO ---")

class ErrorInventario(Exception):
    pass

class ProductoNoEncontrado(ErrorInventario):
    pass

class StockInsuficiente(ErrorInventario):
    pass

class Inventario:
    """Sistema de inventario con manejo completo de excepciones."""

    def __init__(self):
        self.productos = {}

    def agregar_producto(self, codigo, nombre, cantidad):
        """
        Añade producto al inventario.
        - Validar que cantidad sea positiva (ValueError)
        - Validar que codigo no exista ya (KeyError)
        """
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser un número positivo.")
        if codigo in self.productos:
            raise KeyError(f"El código '{codigo}' ya existe en el inventario.")
        self.productos[codigo] = {
            'nombre': nombre,
            'cantidad': cantidad
        }
        print(f"Producto '{nombre}' agregado con código {codigo} (cantidad: {cantidad}).")

    def retirar_stock(self, codigo, cantidad):
        """
        Retira cantidad de un producto.
        - Verificar que producto existe (ProductoNoEncontrado)
        - Verificar que hay suficiente stock (StockInsuficiente)
        """
        if codigo not in self.productos:
            raise ProductoNoEncontrado(f"Producto con código '{codigo}' no encontrado.")
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        disponible = self.productos[codigo]['cantidad']
        if cantidad > disponible:
            raise StockInsuficiente(f"Stock insuficiente: disponible {disponible}, solicitado {cantidad}.")
        self.productos[codigo]['cantidad'] = disponible - cantidad
        print(f"Retirados {cantidad} de '{self.productos[codigo]['nombre']}'. Nuevo stock: {self.productos[codigo]['cantidad']}.")

    def obtener_producto(self, codigo):
        """
        Obtiene información de un producto.
        - Lanzar ProductoNoEncontrado si no existe
        """
        if codigo not in self.productos:
            raise ProductoNoEncontrado(f"Producto con código '{codigo}' no encontrado.")
        return self.productos[codigo]

# Si se ejecuta como script, mostramos pequeñas pruebas
if __name__ == "__main__":
    print("Pruebas rápidas de las funciones implementadas:")
    print("calcular_promedio([1,2,3]) ->", calcular_promedio([1,2,3]))
    print("calcular_promedio([]) ->", calcular_promedio([]))
    print("guardar_datos ->", guardar_datos({'u':'Ana'}, '/tmp/datos_demo.txt'))
    print("procesar_lista_numeros ->", procesar_lista_numeros(['1','2','abc','4']))
    try:
        operacion_critica('0')
    except Exception as e:
        print("operacion_critica: excepción relanzada correctamente.")
