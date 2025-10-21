#!/usr/bin/env python3
"""
PARCIAL 2 - EJERCICIOS (Parte 1)
Estudiante: Estephany Ruales Mazo
Fecha: 18/10/2025
"""
from collections import Counter

# ===========================================================================
# EJERCICIO 1: EXPRESIONES ARITMÉTICAS (10 puntos)
# ===========================================================================

def calculadora_cientifica(operacion, a, b):
    """
    Realiza operaciones aritméticas básicas de forma segura.
    Soporta: suma, resta, multiplicacion, division, potencia, modulo.
    Devuelve el resultado o un mensaje de error si la operación falla.
    """
    try:
        # Verifico que ambos números (a y b) sean int o float
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Los parámetros 'a' y 'b' deben ser numéricos (int o float).")

        # Por si el usuario pone mayúsculas o espacios ...
        operacion = str(operacion).strip().lower()

        # Defino las funciones anonimas para las operaciones válidas
        operaciones = {
            "suma": lambda x, y: x + y,
            "resta": lambda x, y: x - y,
            "multiplicacion": lambda x, y: x * y,
            "division": lambda x, y: x / y,
            "potencia": lambda x, y: x ** y,
            "modulo": lambda x, y: x % y
        }

        # Si la operación no está en el diccionario, lanzamos un error
        if operacion not in operaciones:
            operaciones_validas = ", ".join(operaciones.keys())
            raise ValueError(f"Operación inválida: '{operacion}'. Operaciones válidas: {operaciones_validas}")

        # Validación si se intenta dividir o sacar módulo por cero
        if operacion in ("division", "modulo") and b == 0:
            raise ZeroDivisionError(f"Error matemático: No se puede realizar la operación '{operacion}' por cero.")

        # Ejecuto la operación
        resultado = operaciones[operacion](a, b)

        # Devuelvo el resultado redondeado a 2 decimales
        return float(round(resultado, 2))
      
    except ValueError as ve:
        # Captura errores de tipo de dato o de operación inválida
        return f"Error de valor: {ve}"
        
    except ZeroDivisionError as zde:
        # Captura el error de división por cero
        return f"Error de división: {zde}"
        
    except Exception as e:
        # Capturar cualquier otro error inesperado
        return f"Ha ocurrido un error inesperado: {e}"



# ===========================================================================
# EJERCICIO 2: EXPRESIONES LÓGICAS Y RELACIONALES (12 puntos)
# ===========================================================================

class ValidadorPassword:
    """Validador de contraseñas con reglas configurables."""
    
    def __init__(self, min_longitud=8, requiere_mayuscula=True, 
                 requiere_minuscula=True, requiere_numero=True, 
                 requiere_especial=True):
        """
        Inicializa el validador con reglas específicas.
        """
        self.min_longitud = min_longitud
        self.requiere_mayuscula = requiere_mayuscula
        self.requiere_minuscula = requiere_minuscula
        self.requiere_numero = requiere_numero
        self.requiere_especial = requiere_especial
        self.caracteres_especiales = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
    
    def validar(self, password):
        """
        Valida password según las reglas configuradas.
        """
        erroresP = []
        # Validaciones de errores
        if len(password) < self.min_longitud:
            erroresP.append(f"Longitud mínima no cumplida (mínimo {self.min_longitud} caracteres)")
        if self.requiere_mayuscula and not any(c.isupper() for c in password):
            erroresP.append("Falta al menos una letra mayúscula")
        if self.requiere_minuscula and not any(c.islower() for c in password):
            erroresP.append("Falta al menos una letra minúscula")
        if self.requiere_numero and not any(c.isdigit() for c in password):
            erroresP.append("Falta al menos un número")
        if self.requiere_especial and not any(c in self.caracteres_especiales for c in password):
            erroresP.append("Falta al menos un carácter especial")
        # Devuelve si es valida en un bool y la lista de errores
        return (not erroresP, erroresP)
    
    def es_fuerte(self, password):
        """
        Determina si el password es fuerte.
        """
        # Para ser fuerte, necesita tener 12+ caracteres y cumplir con todas las reglas.
        validadorFuerte = ValidadorPassword(min_longitud=12, requiere_mayuscula=True,
                                             requiere_minuscula=True, requiere_numero=True,
                                             requiere_especial=True)
        es_Fvalido, _ = validadorFuerte.validar(password)
        # Devuelve un bool segun si es o no valida la contraseña
        return es_Fvalido


# ===========================================================================
# EJERCICIO 3: ESTRUCTURAS DE DATOS (15 puntos)
# ===========================================================================

class GestorInventario:
    """Sistema de gestión de inventario."""
    
    def __init__(self):
        """
        Inicializa el inventario. Aquí es donde guardaremos todos nuestros productos.
        """
        self._catalogo_productos = {}
    
    def agregar_producto(self, codigo, nombre, precio, cantidad, categoria):
        """
        Agrega un nuevo tipo de producto a nuestro catálogo.
        """
        # Primero verificamos que dos productos no tengan el mismo código.
        if codigo in self._catalogo_productos:
            raise ValueError(f"El código de producto '{codigo}' ya existe. No se pueden tener duplicados.")
        
        # Si el código es nuevo, lo agregamos a nuestro diccionario.
        self._catalogo_productos[codigo] = {
            'nombre': nombre,
            'precio': float(precio),
            'cantidad': int(cantidad),
            'categoria': categoria
        }
    
    def actualizar_stock(self, codigo, cantidad_cambio):
        """
        Actualiza el stock de un producto.
        """
        if codigo not in self._catalogo_productos:
            raise ValueError(f"Imposible actualizar. Producto con código '{codigo}' no encontrado.")
        stock_final = self._catalogo_productos[codigo]['cantidad'] + cantidad_cambio
        
        # Valida que el stock no puede ser negativo.
        if stock_final < 0:
            raise ValueError("El stock resultante no puede ser negativo. Revisa la cantidad.")
        
        self._catalogo_productos[codigo]['cantidad'] = stock_final
    
    def buscar_por_categoria(self, categoria):
        """
        Busca todos los productos que pertenecen a una categoría específica.
        """
        productos_encontrados = [
            (codigo, detalles_producto['nombre'], detalles_producto['precio'])
            for codigo, detalles_producto in self._catalogo_productos.items()
            if detalles_producto['categoria'] == categoria
        ]
        return productos_encontrados
    
    def productos_bajo_stock(self, limite=10):
        """
        Encuentra productos con stock bajo el límite
        """
        return {
            codigo: detalles['cantidad']
            for codigo, detalles in self._catalogo_productos.items()
            if detalles['cantidad'] < limite
        }
    
    def valor_total_inventario(self):
        """
        Calcula el valor monetario total de todos los productos que tenemos.
        """
        return sum(item['precio'] * item['cantidad'] for item in self._catalogo_productos.values())
    
    def top_productos(self, n=5):
        """
        Retorna los N productos con mayor valor en inventario.
        """
        # valor total de cada tipo de producto en el inventario.
        ranking_de_productos = [
            (codigo, detalles['precio'] * detalles['cantidad'])
            for codigo, detalles in self._catalogo_productos.items()
        ]
        
        # Ordenamos la lista de mayor a menor valor.
        ranking_de_productos.sort(key=lambda producto: producto[1], reverse=True)
        # Devolvemos solo los primeros 'n' productos de la lista ya ordenada.
        return ranking_de_productos[:n]


# ===========================================================================
# EJERCICIO 4: ESTRUCTURAS DE CONTROL (10 puntos)
# ===========================================================================

def es_bisiesto(anio):
    """
    Determina si un año es bisiesto.
    """
    # bool: True si es bisiesto, False en caso contrario
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def dias_en_mes(mes, anio):
    """
    Retorna el número de días en un mes específico.
    """
    # ValueError: Si mes es inválido (no está entre 1 y 12)
    if not 1 <= mes <= 12:
        raise ValueError("El mes debe estar entre 1 y 12.")
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mes == 2 and es_bisiesto(anio):
        return 29
    return dias_por_mes[mes]

def generar_calendario(mes, anio, dia_inicio=0):
    """
    Genera representación string del calendario de un mes.
    """
    # Validamos dia_inicio para que esté siempre en el rango 0-6 (lunes-domingo)
    dia_inicio = dia_inicio % 7
    total_dias = dias_en_mes(mes, anio)
    encabezado = "Lu Ma Mi Ju Vi Sa Do\n"
    cuerpo = ""
    # Se añaden los espacios iniciales según el día de inicio
    cuerpo += "   " * dia_inicio
    
    dia_actual_semana = dia_inicio
    for dia in range(1, total_dias + 1):
        cuerpo += f"{dia: >2}"
        dia_actual_semana += 1
        if dia_actual_semana % 7 == 0:
            if dia < total_dias:
                cuerpo += "\n"
        else:
            # Agregamos un espacio entre días
            cuerpo += " "
    return encabezado + cuerpo.rstrip() 


# ===========================================================================
# EJERCICIO 5: ESTRUCTURAS DE REPETICIÓN (13 puntos)
# ===========================================================================
def analizar_ventas(ventas):
    """
    Analiza lista de ventas y genera estadísticas
    """
    # Si no hubo ventas, no hay nada que analizar. Devolvemos un reporte vacío.
    if not ventas:
        return {}

    # Preparamos nuestras variables para ir acumulando los resultados.
    ingresos_totales = 0.0
    ahorro_total_clientes = 0.0
    popularidad_productos = Counter()
    # Para encontrar la venta más grande, empezamos con una peor venta imaginaria.
    venta_estrella = {'valor_final': -1}

    for cada_venta in ventas:
        valor_bruto = cada_venta['cantidad'] * cada_venta['precio']
        # Calculamos cuánto dinero se le descontó al cliente en esta venta.
        monto_descontado = valor_bruto * cada_venta['descuento']
        # El valor final es lo que realmente pagó el cliente.
        valor_neto_pagado = valor_bruto - monto_descontado

        # Ahora, actualizamos nuestros acumuladores con los datos de esta venta.
        ingresos_totales += valor_neto_pagado
        ahorro_total_clientes += monto_descontado
        popularidad_productos[cada_venta['producto']] += cada_venta['cantidad']

        if valor_neto_pagado > venta_estrella['valor_final']:
            venta_estrella = {'transaccion_completa': cada_venta, 'valor_final': valor_neto_pagado}

    return {
        'total_ventas': round(ingresos_totales, 2),
        'promedio_por_venta': round(ingresos_totales / len(ventas), 2),
        'producto_mas_vendido': popularidad_productos.most_common(1)[0][0],
        'venta_mayor': venta_estrella['transaccion_completa'],
        'total_descuentos': round(ahorro_total_clientes, 2)
    }

def encontrar_patrones(numeros):
    """
    Encuentra patrones en una secuencia de números.
    """
    # Si la lista es muy corta, no pueden existir patrones de secuencia.
    if len(numeros) < 2:
        return {}

    total_rachas_ascendentes, total_rachas_descendentes = 0, 0
    racha_ascendente_mas_larga, racha_descendente_mas_larga = 0, 0
    longitud_racha_actual_asc, longitud_racha_actual_desc = 1, 1

    # Comparamos cada número con el siguiente para ver la tendencia.
    for i in range(len(numeros) - 1):
        if numeros[i+1] > numeros[i]:  
            # Si veníamos de una racha descendente, se rompió. La contamos si era válida (largo >= 2).
            if longitud_racha_actual_desc >= 2: total_rachas_descendentes += 1
            longitud_racha_actual_desc = 1  # Reiniciamos la racha descendente.
            longitud_racha_actual_asc += 1  # Y continuamos la ascendente.

        elif numeros[i+1] < numeros[i]:  # La secuencia baja
            # Se rompió una posible racha ascendente. La contamos si fue válida.
            if longitud_racha_actual_asc >= 2: total_rachas_ascendentes += 1
            longitud_racha_actual_asc = 1   # Reiniciamos la racha ascendente.
            longitud_racha_actual_desc += 1 # Y continuamos la descendente.
        else:  # Los números son iguales, ambas rachas se rompen.
            if longitud_racha_actual_asc >= 2: total_rachas_ascendentes += 1
            if longitud_racha_actual_desc >= 2: total_rachas_descendentes += 1
            longitud_racha_actual_asc, longitud_racha_actual_desc = 1, 1
        
        # En cada paso, actualizamos cuál ha sido la racha más larga vista hasta ahora.
        racha_ascendente_mas_larga = max(racha_ascendente_mas_larga, longitud_racha_actual_asc)
        racha_descendente_mas_larga = max(racha_descendente_mas_larga, longitud_racha_actual_desc)

    if longitud_racha_actual_asc >= 2: total_rachas_ascendentes += 1
    if longitud_racha_actual_desc >= 2: total_rachas_descendentes += 1
    
    frecuencia_de_numeros = Counter(numeros)
    # Nos quedamos solo con los que aparecieron más de una vez.
    duplicados_encontrados = {num: count for num, count in frecuencia_de_numeros.items() if count > 1}

    return {
        'secuencias_ascendentes': total_rachas_ascendentes,
        'secuencias_descendentes': total_rachas_descendentes,
        'longitud_max_ascendente': racha_ascendente_mas_larga if racha_ascendente_mas_larga > 1 else 0,
        'longitud_max_descendente': racha_descendente_mas_larga if racha_descendente_mas_larga > 1 else 0,
        'numeros_repetidos': duplicados_encontrados
    }

def simular_crecimiento(inversion_inicial, interes_anual_decimal, periodo_en_anios, contribucion_anual=0):
    """
    Simula crecimiento de inversión con interés compuesto.
    """
    proyeccion_anual = []
    capital_acumulado = inversion_inicial

    for anio_actual in range(1, periodo_en_anios + 1):
        # Al empezar un nuevo año, primero se añade la contribución.
        base_para_interes = capital_acumulado + contribucion_anual

        # Luego, calculamos la ganancia de ese año sobre el nuevo total.
        ganancia_por_interes = base_para_interes * interes_anual_decimal
        
        # Y finalmente, actualizamos nuestro capital total para el final del año.
        capital_acumulado = base_para_interes + ganancia_por_interes

        # Guardamos el resumen de este año en nuestro historial.
        proyeccion_anual.append({
            'anio': anio_actual,
            'balance': round(capital_acumulado, 2),
            'interes_ganado': round(ganancia_por_interes, 2)
        })

    return proyeccion_anual


# ===========================================================================
# CASOS DE PRUEBA
# ===========================================================================

if __name__ == "__main__":
    print("="*70)
    print(" PRUEBAS DE EJERCICIOS")
    print("="*70)
    
    # Aquí puedes añadir tus propias pruebas
    
    print("\nEjercicio 1: Calculadora")
    # Pruebas
    print(calculadora_cientifica("division", 10, 3))  # Retorna: 3.33
    print(calculadora_cientifica("potencia", 2, 8))   # Retorna: 256.0
    print(calculadora_cientifica("division", 10, 0))  # Lanza ZeroDivisionError
    print(calculadora_cientifica("raiz", 4, 2))       # Lanza ValueError

    print("\nEjercicio 2: Validador de Password")
    # Pruebas
    validador = ValidadorPassword(min_longitud=8)
    print(validador.validar("Abc123!"))         # (False, ['Longitud mínima no cumplida'])
    print(validador.validar("Abc123!@"))        # (True, [])
    print(validador.validar("abcdefgh"))        # (False, ['Falta mayúscula', ...])
    print(validador.es_fuerte("Abc123!@#$Xyz")) # True
    
    print("\nEjercicio 3: Gestor de Inventario")
    # Pruebas
    inv = GestorInventario()
    inv.agregar_producto("P001", "Laptop", 1200.00, 15, "Electrónica")
    inv.agregar_producto("P002", "Mouse", 25.50, 5, "Accesorios")
    inv.agregar_producto("P003", "Teclado", 85.00, 8, "Accesorios")

    inv.actualizar_stock("P001", -3)  # Reduce stock
    print(inv.productos_bajo_stock(10))  # {'P002': 5, 'P003': 8}
    print(inv.buscar_por_categoria("Accesorios"))  # [('P002', 'Mouse', 25.5), ...]
    print(inv.valor_total_inventario())  # Suma total
    print(inv.top_productos(2))  # Top 2 productos por valor
        
    print("\nEjercicio 4: Calendario")
    # Pruebas
    print(es_bisiesto(2024))  # True
    print(es_bisiesto(2100))  # False
    print(es_bisiesto(2000))  # True
    print(dias_en_mes(2, 2024))  # 29
    print(dias_en_mes(2, 2023))  # 28
    print(generar_calendario(1, 2024, 0))  # Calendario de enero 2024
    
    print("\nEjercicio 5: Análisis de Datos")
    # Pruebas
    ventas = [
    {'producto': 'Laptop', 'cantidad': 2, 'precio': 1000, 'descuento': 0.1},
    {'producto': 'Mouse', 'cantidad': 10, 'precio': 20, 'descuento': 0.0},
    {'producto': 'Laptop', 'cantidad': 3, 'precio': 1000, 'descuento': 0.15}
    ]
    print(analizar_ventas(ventas))

    numeros = [1, 2, 3, 2, 1, 2, 3, 4, 5, 3, 3, 3]
    print(encontrar_patrones(numeros))

    print(simular_crecimiento(1000, 0.05, 5, 100))
