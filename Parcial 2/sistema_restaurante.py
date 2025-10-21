#!/usr/bin/env python3
"""
PARCIAL 2 - PROBLEMA INTEGRADOR (Parte 2)
Sistema de Gestión de Restaurante

Autor: Estephany Ruales Mazo
Fecha: 19/10/2025
"""
from datetime import datetime
import os

# ===========================================================================
# EXCEPCIONES PERSONALIZADAS
# ===========================================================================

class ErrorRestaurante(Exception):
    """Excepción base para el sistema de restaurante."""
    pass


class PlatoNoEncontrado(ErrorRestaurante):
    """Se lanza cuando un plato no existe en el menú."""
    def __init__(self, codigo_plato):
        super().__init__(f"Plato con código '{codigo_plato}' no encontrado en el menú")


class MesaNoDisponible(ErrorRestaurante):
    """Se lanza cuando la mesa está ocupada."""
    def __init__(self, numero_mesa, hora_disponible="desconocida"):
        super().__init__(f"Mesa {numero_mesa} no disponible. Disponible a las {hora_disponible}")


class CapacidadExcedida(ErrorRestaurante):
    """Se lanza cuando hay más comensales que capacidad."""
    def __init__(self, numero_mesa, capacidad, comensales):
        super().__init__(f"Mesa {numero_mesa} tiene capacidad para {capacidad}, "
                         f"pero se solicitaron {comensales} lugares.")


class PedidoInvalido(ErrorRestaurante):
    """Se lanza para pedidos con problemas."""
    def __init__(self, razon):
        super().__init__(f"Pedido inválido: {razon}")


# ===========================================================================
# CLASE PRINCIPAL: SISTEMA RESTAURANTE
# ===========================================================================

class SistemaRestaurante:
    """Sistema completo de gestión de restaurante."""

    VALID_CATEGORIAS = {"entrada", "plato_fuerte", "postre", "bebida"}

    def __init__(self, num_mesas=10, tasa_impuesto=0.16, propina_sugerida=0.15):
        self.num_mesas = num_mesas
        self.tasa_impuesto = tasa_impuesto
        self.propina_sugerida = propina_sugerida

        # Estructuras principales
        self.menu = {}
        self.mesas = {
            i: {"capacidad": 0, "disponible": True, "reserva": None, "pedido_actual": None}
            for i in range(1, num_mesas + 1)
        }
        self.pedidos = {}
        self.pedidos_pagados = []
        self.ventas_count = {}
        self.ventas_por_cat = {}

    # ================== MENÚ ==================

    def agregar_plato(self, codigo, nombre, categoria, precio):
        """Agrega un plato al menú o actualiza si ya existe."""
        if not codigo or not nombre:
            raise ValueError("Código y nombre son obligatorios")
        if categoria not in self.VALID_CATEGORIAS:
            raise ValueError(f"Categoría inválida. Debe ser una de {self.VALID_CATEGORIAS}")
        try:
            precio = float(precio)
        except ValueError:
            raise ValueError("Precio inválido")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0")

        self.menu[codigo] = {
            "nombre": nombre,
            "categoria": categoria,
            "precio": round(precio, 2),
            "disponible": True
        }

    def cambiar_disponibilidad(self, codigo, disponible):
        """Cambia la disponibilidad de un plato."""
        if codigo not in self.menu:
            raise PlatoNoEncontrado(codigo)
        self.menu[codigo]["disponible"] = bool(disponible)

    def buscar_platos(self, categoria=None, precio_max=None):
        """Busca platos disponibles filtrando por categoría o precio."""
        resultados = []
        for cod, info in self.menu.items():
            if not info["disponible"]:
                continue
            if categoria and info["categoria"] != categoria:
                continue
            if precio_max and info["precio"] > float(precio_max):
                continue
            resultados.append({
                "codigo": cod, "nombre": info["nombre"], "categoria": info["categoria"],
                "precio": info["precio"], "disponible": info["disponible"]
            })
        return resultados

    # ================== MESAS ==================

    def configurar_mesa(self, numero, capacidad):
        """Asigna la capacidad de una mesa."""
        if numero not in self.mesas:
            raise ValueError("Número de mesa inválido")
        if not 1 <= capacidad <= 12:
            raise ValueError("La capacidad debe estar entre 1 y 12")
        self.mesas[numero]["capacidad"] = capacidad

    def reservar_mesa(self, numero, comensales, hora):
        """Reserva una mesa para una cantidad de comensales."""
        if numero not in self.mesas:
            raise ValueError("Mesa inexistente")
        
        # CORREGIDO: Se añade validación del formato de hora
        try:
            datetime.strptime(hora, '%H:%M')
        except ValueError:
            raise ValueError("El formato de la hora debe ser 'HH:MM'")

        mesa = self.mesas[numero]
        if not mesa["disponible"]:
            raise MesaNoDisponible(numero, mesa["reserva"])
        if comensales > mesa["capacidad"]:
            raise CapacidadExcedida(numero, mesa["capacidad"], comensales)

        mesa["disponible"] = False
        mesa["reserva"] = hora

    def liberar_mesa(self, numero):
        """Libera una mesa (termina servicio)."""
        if numero not in self.mesas:
            raise ValueError("Mesa inexistente")
        
        mesa = self.mesas[numero]
        # CORREGIDO: Se valida que la mesa estuviera ocupada
        if mesa["disponible"]:
            raise ValueError(f"La mesa {numero} ya está libre.")
            
        mesa["disponible"] = True
        mesa["reserva"] = None
        # CORREGIDO: Se desvincula el pedido de la mesa
        mesa["pedido_actual"] = None

    def mesas_disponibles(self, comensales):
        """Devuelve lista de mesas disponibles para N comensales."""
        return [
            num for num, m in self.mesas.items()
            if m["disponible"] and m["capacidad"] >= comensales
        ]

    # ================== PEDIDOS ==================

    def crear_pedido(self, numero_mesa):
        """Crea un nuevo pedido para una mesa."""
        if numero_mesa not in self.mesas:
            raise ValueError("Mesa inexistente")
        
        mesa = self.mesas[numero_mesa]
        if mesa["disponible"]:
            raise MesaNoDisponible(numero_mesa)
        
        # CORREGIDO: Se valida que la mesa no tenga ya un pedido activo
        if mesa["pedido_actual"] is not None:
            raise PedidoInvalido(f"La mesa {numero_mesa} ya tiene el pedido activo {mesa['pedido_actual']}")
        
        pedido_id = f"P{len(self.pedidos) + len(self.pedidos_pagados) + 1:03d}"
        self.pedidos[pedido_id] = {
            "id_mesa": numero_mesa, "items": {}, "pagado": False
        }
        # CORREGIDO: Se asigna el nuevo pedido a la mesa
        mesa["pedido_actual"] = pedido_id
        return pedido_id

    def agregar_item(self, id_pedido, codigo_plato, cantidad=1):
        """Agrega ítems a un pedido."""
        if id_pedido not in self.pedidos:
            raise PedidoInvalido("El pedido no existe o ya fue pagado.")
        if codigo_plato not in self.menu:
            raise PlatoNoEncontrado(codigo_plato)
        if not self.menu[codigo_plato]["disponible"]:
            raise ValueError("Plato no disponible")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")

        pedido = self.pedidos[id_pedido]
        pedido["items"][codigo_plato] = pedido["items"].get(codigo_plato, 0) + cantidad

    def calcular_total(self, id_pedido, propina_porcentaje=None):
        """Calcula el total de un pedido."""
        if id_pedido not in self.pedidos:
            raise PedidoInvalido("El pedido no existe.")
        
        pedido = self.pedidos[id_pedido]
        subtotal = sum(self.menu[c]["precio"] * cant for c, cant in pedido["items"].items())
        impuesto = subtotal * self.tasa_impuesto
        propina_ratio = propina_porcentaje if propina_porcentaje is not None else self.propina_sugerida
        propina = subtotal * propina_ratio
        total = subtotal + impuesto + propina
        return {
            "subtotal": round(subtotal, 2), "impuesto": round(impuesto, 2),
            "propina": round(propina, 2), "total": round(total, 2)
        }

    def pagar_pedido(self, id_pedido, propina_porcentaje=None):
        """Procesa el pago de un pedido."""
        if id_pedido not in self.pedidos:
            raise PedidoInvalido("El pedido no existe o ya fue pagado.")
        
        totales = self.calcular_total(id_pedido, propina_porcentaje)

        # movemos el pedido de 'activos' a 'pagados'.
        pedido_a_pagar = self.pedidos.pop(id_pedido)

        # Actualizamos el diccionario del pedido con los totales y el estado.
        pedido_a_pagar.update(totales)
        pedido_a_pagar["pagado"] = True
        self.pedidos_pagados.append(pedido_a_pagar)

        # Actualizamos contadores de ventas.
        for cod, cant in pedido_a_pagar["items"].items():
            self.ventas_count[cod] = self.ventas_count.get(cod, 0) + cant
            cat = self.menu[cod]["categoria"]
            precio_item = self.menu[cod]["precio"]
            self.ventas_por_cat[cat] = self.ventas_por_cat.get(cat, 0.0) + (precio_item * cant)

        # Devolvemos la cadena de texto con el resumen del pago.
        return f"Pedido {id_pedido} pagado correctamente por un total de ${totales['total']:.2f}"

    # ================== REPORTES ==================

    def platos_mas_vendidos(self, n=5):
        """Devuelve los N platos más vendidos."""
        ordenados = sorted(self.ventas_count.items(), key=lambda x: x[1], reverse=True)
        return [
            {"plato": self.menu[c]["nombre"], "cantidad": v}
            for c, v in ordenados[:n]
        ]

    def ventas_por_categoria(self):
        """Devuelve el total vendido por categoría."""
        return {cat: round(v, 2) for cat, v in self.ventas_por_cat.items()}

    def reporte_ventas_dia(self):
        """
        Genera reporte completo de ventas del día con todos los campos requeridos.
        """
        if not self.pedidos_pagados:
            return {
                'total_pedidos': 0, 'subtotal_ventas': 0.0, 'total_impuestos': 0.0,
                'total_propinas': 0.0, 'total_ingresos': 0.0, 'ticket_promedio': 0.0,
                'plato_mas_vendido': "N/A"
            }

        total_pedidos = len(self.pedidos_pagados)
        subtotal_ventas = sum(p['subtotal'] for p in self.pedidos_pagados)
        total_impuestos = sum(p['impuesto'] for p in self.pedidos_pagados)
        total_propinas = sum(p['propina'] for p in self.pedidos_pagados)
        total_ingresos = sum(p['total'] for p in self.pedidos_pagados)
        ticket_promedio = total_ingresos / total_pedidos if total_pedidos > 0 else 0
        
        mas_vendidos = self.platos_mas_vendidos(n=1)
        plato_mas_vendido = mas_vendidos[0]['plato'] if mas_vendidos else "N/A"
        
        return {
            'total_pedidos': total_pedidos,
            'subtotal_ventas': round(subtotal_ventas, 2),
            'total_impuestos': round(total_impuestos, 2),
            'total_propinas': round(total_propinas, 2),
            'total_ingresos': round(total_ingresos, 2),
            'ticket_promedio': round(ticket_promedio, 2),
            'plato_mas_vendido': plato_mas_vendido
        }

    def estado_restaurante(self):
        """Devuelve un resumen general del estado actual."""
        return {
            "mesas_disponibles": sum(1 for m in self.mesas.values() if m["disponible"]),
            "mesas_ocupadas": sum(1 for m in self.mesas.values() if not m["disponible"]),
            "pedidos_activos": len(self.pedidos),
            "pedidos_completados_hoy": len(self.pedidos_pagados)
        }

    # ================== IMPORTAR / EXPORTAR (Implementación) ==================
    def exportar_menu(self, archivo='menu_exportado.txt'):
        """
        Exporta el menú completo al archivo, sobrescribiéndolo.
        Utiliza una ruta absoluta para evitar problemas de ubicación.
        """
        try:
            directorio_script = os.path.dirname(os.path.abspath(__file__))
            ruta_completa = os.path.join(directorio_script, archivo)
            
            with open(ruta_completa, 'w', encoding='utf-8') as f:
                for codigo, info in self.menu.items():
                    f.write(
                        f"{codigo}|{info['nombre']}|{info['categoria']}|"
                        f"{info['precio']}|{info['disponible']}\n"
                    )
            return True
        except IOError as e:
            print(f"Error al exportar el menú: {e}")
            return False

    def importar_menu(self, archivo='menu_inicial.txt'):
        """
        Importa el menú desde un archivo, limpiando los datos previos.
        Utiliza una ruta absoluta para ser más robusto.
        """
        resultado = {'exitosos': 0, 'errores': []}
        self.menu.clear()
        
        try:
            directorio_script = os.path.dirname(os.path.abspath(__file__))
            ruta_completa = os.path.join(directorio_script, archivo)

            with open(ruta_completa, 'r', encoding='utf-8') as f:
                for i, linea in enumerate(f, 1):
                    if not linea.strip(): continue
                    partes = linea.strip().split('|')
                    if len(partes) != 5:
                        resultado['errores'].append((i, "Formato incorrecto (se esperaban 5 campos)."))
                        continue
                    
                    codigo, nombre, categoria, precio_str, disponible_str = partes
                    if codigo in self.menu:
                        resultado['errores'].append((i, f"Código '{codigo}' duplicado (saltado)."))
                        continue
                        
                    try:
                        self.agregar_plato(codigo, nombre, categoria, float(precio_str))
                        self.menu[codigo]['disponible'] = disponible_str.lower() == 'true'
                        resultado['exitosos'] += 1
                    except ValueError as e:
                        resultado['errores'].append((i, str(e)))
        except FileNotFoundError:
            resultado['errores'].append((0, f"El archivo '{ruta_completa}' no fue encontrado."))
            
        return resultado
    
    def cargar_menu_desde_archivo(self, archivo="menu_inicial.txt"):
        """Alias para importar_menu, usado por las pruebas."""
        print(f"\nIntentando cargar menú desde '{archivo}'...")
        resultado = self.importar_menu(archivo)
        
        if resultado['exitosos'] > 0:
            print(f"✓ Se cargaron {resultado['exitosos']} platos exitosamente.")
        
        if resultado['errores']:
            print("⚠ Se encontraron los siguientes problemas:")
            for linea, error in resultado['errores']:
                if linea == 0:
                    print(f"  - Error general: {error}")
                else:
                    print(f"  - Línea {linea}: {error}")