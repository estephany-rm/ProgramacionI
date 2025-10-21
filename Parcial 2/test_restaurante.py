"""
PARCIAL 2 - CASOS DE PRUEBA
Sistema de Gestion de Restaurante

Estudiante: Estephany Ruales Mazo
Fecha: 19/10/2025
"""
from sistema_restaurante import *
import os

# ===============================================================
# AGREGAR PLATOS Y CONFIGURAR MESAS
# ===============================================================
def prueba_agregar_platos_y_configurar_mesas():
    """Prueba agregar platos y configurar mesas."""
    print("\n" + "="*60)
    print(" TEST: Agregar Platos y Configurar Mesas")
    print("="*60)
    
    restaurante = SistemaRestaurante(num_mesas=3, tasa_impuesto=0.16, propina_sugerida=0.10)
    
    # Agregar plato válido
    restaurante.agregar_plato("C001", "Ramen", "plato_fuerte", 450.00)
    assert "C001" in restaurante.menu
    print("✓ PASÓ: Se agregó un plato válido correctamente.")
    
    # Intentar agregar plato duplicado
    restaurante.agregar_plato("P001", "Filete de Lomo", "plato_fuerte", 450.00)
    assert restaurante.menu["P001"]["precio"] == 450.00
    print("✓ PASÓ: Se actualizó un plato con ID duplicado.")

    # Configurar mesa válida
    restaurante.configurar_mesa(1, 4)
    assert restaurante.mesas[1]["capacidad"] == 4
    print("✓ PASÓ: Se configuró una mesa correctamente.")
    
    print("✓ Prueba completada")


# ===============================================================
# RESERVAR MESA Y CREAR PEDIDOS
# ===============================================================
def prueba_reservar_y_crear_pedidos():
    """Prueba reservar y crear pedidos."""
    print("\n" + "="*60)
    print(" TEST: Reservar Mesas y Crear Pedidos")
    print("="*60)
    
    restaurante = SistemaRestaurante(num_mesas=2, tasa_impuesto=0.16, propina_sugerida=0.10)
    restaurante.configurar_mesa(1, 4)
    restaurante.configurar_mesa(2, 2)
    
    # Reserva exitosa
    restaurante.reservar_mesa(1, 3, "20:00")
    assert not restaurante.mesas[1]["disponible"]
    print("✓ PASÓ: Se reservó una mesa exitosamente.")

    # Crear un pedido para la mesa reservada
    id_pedido = restaurante.crear_pedido(1)
    assert id_pedido in restaurante.pedidos
    assert restaurante.pedidos[id_pedido]["id_mesa"] == 1
    print(f"✓ PASÓ: Se creó el pedido {id_pedido} para la mesa 1.")

    # Intentar reservar mesa ocupada
    try:
        restaurante.reservar_mesa(1, 2, "20:30")
        assert False, "No se lanzó MesaNoDisponible"
    except MesaNoDisponible:
        print("✓ PASÓ: Se evitó reservar una mesa ya ocupada.")

    print("✓ Prueba completada")


# ===============================================================
# AGREGAR ÍTEMS Y CALCULAR TOTAL
# ===============================================================
def prueba_agregar_items_y_calcular_total():
    """Prueba agregar items y calcular total."""
    print("\n" + "="*60)
    print(" TEST: Agregar Ítems y Calcular Total")
    print("="*60)
    
    restaurante = SistemaRestaurante(num_mesas=1, tasa_impuesto=0.10, propina_sugerida=0.15)
    restaurante.configurar_mesa(1, 2)
    restaurante.agregar_plato("P001", "Filete", "plato_fuerte", 300.0)
    restaurante.agregar_plato("B001", "Refresco", "bebida", 50.0)
    
    restaurante.reservar_mesa(1, 2, "19:00")
    id_pedido = restaurante.crear_pedido(1)
    
    # Agregar ítems
    restaurante.agregar_item(id_pedido, "P001", 1)
    restaurante.agregar_item(id_pedido, "B001", 2)
    print("✓ PASÓ: Se agregaron ítems al pedido.")

    # Calcular total esperado
    totales = restaurante.calcular_total(id_pedido)
    assert totales['subtotal'] == 400.0
    assert totales['impuesto'] == 40.0
    assert totales['propina'] == 60.0
    assert totales['total'] == 500.0
    print(f"✓ PASÓ: El cálculo del total ({totales['total']}) es correcto.")

    print("✓ Prueba completada")


# ===============================================================
# PAGAR PEDIDO Y LIBERAR MESA
# ===============================================================
def prueba_pagar_y_liberar_mesa():
    """Prueba pagar pedido y liberar mesa."""
    print("\n" + "="*60)
    print(" TEST: Pagar Pedido y Liberar Mesa")
    print("="*60)

    restaurante = SistemaRestaurante(num_mesas=1, tasa_impuesto=0.16, propina_sugerida=0.10)
    restaurante.configurar_mesa(1, 2)
    restaurante.agregar_plato("E001", "Ensalada", "entrada", 100.0)

    restaurante.reservar_mesa(1, 2, "13:00")
    id_pedido = restaurante.crear_pedido(1)
    restaurante.agregar_item(id_pedido, "E001", 2)

    # Pagar pedido
    resultado_pago = restaurante.pagar_pedido(id_pedido)
    # Verificar que la cadena de texto contenga el mensaje esperado.
    assert "pagado correctamente" in resultado_pago
    assert restaurante.pedidos_pagados[-1]["pagado"]
    print("✓ PASÓ: El pedido se marcó como pagado.")

    # Liberar mesa
    restaurante.liberar_mesa(1)
    assert restaurante.mesas[1]["disponible"]
    assert restaurante.mesas[1]["reserva"] is None
    print("✓ PASÓ: La mesa se liberó correctamente.")

    print("✓ Prueba completada")


# ===============================================================
# REPORTES DE VENTAS
# ===============================================================
def prueba_reportes_de_ventas():
    """Prueba reportes de ventas."""
    print("\n" + "="*60)
    print(" TEST: Reportes de Ventas")
    print("="*60)
    
    restaurante = SistemaRestaurante(num_mesas=2, tasa_impuesto=0.10, propina_sugerida=0.10)
    restaurante.cargar_menu_desde_archivo("menu_inicial.txt")
    restaurante.configurar_mesa(1, 2)
    restaurante.configurar_mesa(2, 2)

    # Pedido 1
    restaurante.reservar_mesa(1, 2, "14:00")
    p1 = restaurante.crear_pedido(1)
    restaurante.agregar_item(p1, "P001", 2)
    restaurante.pagar_pedido(p1)
    restaurante.liberar_mesa(1)

    # Pedido 2
    restaurante.reservar_mesa(2, 2, "14:30")
    p2 = restaurante.crear_pedido(2)
    restaurante.agregar_item(p2, "P001", 1)
    restaurante.agregar_item(p2, "D001", 3)
    restaurante.pagar_pedido(p2)
    restaurante.liberar_mesa(2)

    # Platos más vendidos
    mas_vendidos = restaurante.platos_mas_vendidos(2)
    assert mas_vendidos[0]["plato"] and mas_vendidos[1]["plato"]
    print("✓ PASÓ: El reporte de platos más vendidos es correcto.")
    
    # Ventas por categoría
    ventas_cat = restaurante.ventas_por_categoria()
    assert isinstance(ventas_cat, dict)
    print("✓ PASÓ: El reporte de ventas por categoría es correcto.")

    print("✓ Prueba completada")


# ===============================================================
# MANEJO DE EXCEPCIONES
# ===============================================================
def prueba_manejo_de_excepciones():
    """Prueba manejo de excepciones."""
    print("\n" + "="*60)
    print(" TEST: Manejo de Excepciones")
    print("="*60)
    
    restaurante = SistemaRestaurante(num_mesas=1, tasa_impuesto=0.16, propina_sugerida=0.10)
    restaurante.configurar_mesa(1, 2)
    
    try:
        restaurante.reservar_mesa(1, 2, "18:00")
        id_pedido = restaurante.crear_pedido(1)
        restaurante.agregar_item(id_pedido, "X999", 1)
        assert False, "No se lanzó PlatoNoEncontrado"
    except PlatoNoEncontrado:
        print("✓ PASÓ: Se detectó correctamente un plato no encontrado.")
    
    try:
        restaurante.liberar_mesa(1)
        restaurante.reservar_mesa(1, 5, "20:00")
        assert False, "No se lanzó CapacidadExcedida"
    except CapacidadExcedida:
        print("✓ PASÓ: Se detectó correctamente el exceso de capacidad.")
        
    print("✓ Prueba completada")


# ===============================================================
# IMPORTAR Y EXPORTAR MENÚ
# ===============================================================
def prueba_importar_exportar_menu():
    """Prueba importar y exportar menu."""
    print("\n" + "="*60)
    print(" TEST: Importar y Exportar Menú")
    print("="*60)
    
    restaurante = SistemaRestaurante(num_mesas=1, tasa_impuesto=0.1, propina_sugerida=0.1)
    restaurante.importar_menu("menu_inicial.txt")
    restaurante.agregar_plato("T001", "Taco de Pastor", "plato_fuerte", 25.0)
    restaurante.agregar_plato("T002", "Gringa", "plato_fuerte", 40.0)
    
    archivo_exportado = "menu_test_export.txt"
    restaurante.exportar_menu(archivo_exportado)
    print(f"✓ PASÓ: Menú exportado a '{archivo_exportado}'.")
    
    nuevo_restaurante = SistemaRestaurante(num_mesas=1, tasa_impuesto=0.1, propina_sugerida=0.1)
    nuevo_restaurante.cargar_menu_desde_archivo(archivo_exportado)
    
    assert "T001" in nuevo_restaurante.menu
    assert nuevo_restaurante.menu["T002"]["nombre"] == "Gringa"
    print("✓ PASÓ: Menú importado correctamente desde archivo.")
    
    print("✓ Prueba completada")


# ===============================================================
# EJECUTAR TODAS LAS PRUEBAS
# ===============================================================
def ejecutar_todas_las_pruebas():
    print("\n" + "="*70)
    print(" EJECUTANDO SUITE COMPLETA DE PRUEBAS PARA SISTEMA RESTAURANTE")
    print("="*70)
    
    pruebas = [
        prueba_agregar_platos_y_configurar_mesas,
        prueba_reservar_y_crear_pedidos,
        prueba_agregar_items_y_calcular_total,
        prueba_pagar_y_liberar_mesa,
        prueba_reportes_de_ventas,
        prueba_manejo_de_excepciones,
        prueba_importar_exportar_menu,
    ]
    
    exitosas = 0
    fallidas = 0
    
    for prueba in pruebas:
        try:
            prueba()
            exitosas += 1
        except Exception as e:
            print(f"\n✗ ERROR EN {prueba.__name__}: {e}\n")
            fallidas += 1
    
    print("\n" + "="*70)
    print(" RESUMEN DE PRUEBAS")
    print("="*70)
    print(f"✓ Exitosas: {exitosas}/{len(pruebas)}")
    print(f"✗ Fallidas: {fallidas}/{len(pruebas)}")
    print("="*70)


# ===============================================================
# MAIN
# ===============================================================
if __name__ == "__main__":
    ejecutar_todas_las_pruebas()
