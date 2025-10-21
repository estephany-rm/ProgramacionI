#!/usr/bin/env python3
"""
PARCIAL 2 - CASOS DE PRUEBA
Sistema de Biblioteca Digital

Estudiante: Estephany Ruales Mazo
Fecha: 18/10/2025
"""
from datetime import datetime, timedelta
from sistema_biblioteca import *

def prueba_agregar_libros():
    """Prueba agregar libros al catálogo."""
    print("\n" + "="*60)
    print(" TEST: Agregar Libros")
    print("="*60)
    
    biblioteca = SistemaBiblioteca()
    
    # Agregar libro válido
    biblioteca.agregar_libro("9780134685991", "Effective Python", "Brett Slatkin", 2019, "Programación", 3)
    assert "9780134685991" in biblioteca.catalogo
    print("✓ PASÓ: Se agregó un libro válido correctamente.")
    
    # Intentar agregar libro duplicado
    try:
        biblioteca.agregar_libro("9780134685991", "Otro Título", "Otro Autor", 2020, "Test", 1)
        assert False, "No se lanzó KeyError por ISBN duplicado"
    except KeyError:
        print("✓ PASÓ: Se evitó agregar un libro duplicado.")
    
    # Agregar libro con ISBN inválido
    try:
        biblioteca.agregar_libro("123", "Libro Inválido", "Autor", 2020, "Error", 1)
    except ValueError:
        print("✓ PASÓ: Se detectó ISBN inválido correctamente.")
    
    # Agregar libro con año inválido
    try:
        biblioteca.agregar_libro("9780134685000", "Libro Antiguo", "Autor", 1500, "Error", 1)
    except ValueError:
        print("✓ PASÓ: Se detectó año inválido correctamente.")
    
    print("✓ Prueba completada")


def prueba_registrar_usuarios():
    """Prueba registro de usuarios."""
    print("\n" + "="*60)
    print(" TEST: Registrar Usuarios")
    print("="*60)
    
    biblioteca = SistemaBiblioteca()
    
    # Registrar usuario válido
    biblioteca.registrar_usuario("U001", "Ana Pérez", "ana@correo.com")
    assert "U001" in biblioteca.usuarios
    print("✓ PASÓ: Se registró un usuario válido.")
    
    # Usuario duplicado
    try:
        biblioteca.registrar_usuario("U001", "Ana Pérez", "ana@correo.com")
        assert False, "No se lanzó la excepción por usuario duplicado."
    except ValueError:
        print("✓ PASÓ: Se evitó registrar un usuario duplicado.")
    
    # Email inválido
    try:
        biblioteca.registrar_usuario("U002", "Carlos López", "correo_invalido")
    except ValueError:
        print("✓ PASÓ: Se detectó email inválido correctamente.")
    
    print("✓ Prueba completada")

def prueba_prestar_libros():
    """Prueba sistema de préstamos."""
    print("\n" + "="*60)
    print(" TEST: Préstamos")
    print("="*60)
    
    biblioteca = SistemaBiblioteca(limite_prestamos=2)
    biblioteca.agregar_libro("9780134685991", "Effective Python", "Brett Slatkin", 2019, "Programación", 1)
    biblioteca.registrar_usuario("U001", "Ana Pérez", "ana@correo.com")
    
    # Préstamo exitoso
    id_prestamo = biblioteca.prestar_libro("9780134685991", "U001")
    print(f"✓ PASÓ: Préstamo exitoso ({id_prestamo}).")
    
    # Intentar prestar libro no disponible
    try:
        biblioteca.prestar_libro("9780134685991", "U001")
    except LibroNoDisponible:
        print("✓ PASÓ: Se controló préstamo de libro sin copias disponibles.")
    
    # Exceder límite de préstamos
    biblioteca.agregar_libro("9780135404676", "Python Crash Course", "Eric Matthes", 2019, "Programación", 2)
    biblioteca.prestar_libro("9780135404676", "U001")
    try:
        biblioteca.agregar_libro("9781449355739", "Fluent Python", "Luciano Ramalho", 2015, "Programación", 1)
        biblioteca.prestar_libro("9781449355739", "U001")
    except LimitePrestamosExcedido:
        print("✓ PASÓ: Se controló el límite de préstamos por usuario.")
    
    # Usuario no registrado
    try:
        biblioteca.prestar_libro("9781449355739", "U999")
    except UsuarioNoRegistrado:
        print("✓ PASÓ: Se detectó intento de préstamo con usuario inexistente.")
    
    print("✓ Prueba completada")

def prueba_devolver_libros():
    """Prueba devolución y cálculo de multas."""
    print("\n" + "="*60)
    print(" TEST: Devolución y Multas")
    print("="*60)
    
    biblioteca = SistemaBiblioteca(multa_por_dia=2.0, dias_prestamo=7)
    
    # Agregar libro y usuario
    biblioteca.agregar_libro("9780321765723", "The C++ Programming Language", "Bjarne Stroustrup", 2013, "Programación", 2)
    biblioteca.registrar_usuario("USR001", "Ada Lovelace", "ada@example.com")
    
    # --- Caso 1: Devolución a tiempo (sin multa) ---
    id_prestamo_1 = biblioteca.prestar_libro("9780321765723", "USR001")
    resultado = biblioteca.devolver_libro(id_prestamo_1)
    assert resultado['multa'] == 0.0, "Falla: Devolución a tiempo no debería tener multa."
    print("✓ PASÓ: Devolución a tiempo (sin multa).")
    
    # --- Caso 2: Devolución con retraso (con multa) ---
    id_prestamo_2 = biblioteca.prestar_libro("9780321765723", "USR001")
    
    # Hacemos que el préstamo parezca 5 días vencido
    prestamo_vencido = biblioteca.prestamos[id_prestamo_2]
    prestamo_vencido['fecha_vencimiento'] = datetime.now() - timedelta(days=5)
    
    resultado_multa = biblioteca.devolver_libro(id_prestamo_2)
    multa_esperada = 5 * 2.0
    assert resultado_multa['multa'] == multa_esperada, f"Falla: La multa debería ser {multa_esperada}."
    print("✓ PASÓ: Devolución con retraso calculó la multa correctamente.")

    # --- Caso 3: Intentar devolver préstamo inexistente ---
    try:
        biblioteca.devolver_libro("P_INEXISTENTE")
        assert False, "Falla: Debería lanzar KeyError para préstamo inexistente."
    except KeyError:
        print("✓ PASÓ: Se manejó correctamente el intento de devolver un préstamo inexistente.")
    
    print("✓ Prueba completada")

def prueba_buscar_libros():
    """Prueba búsqueda de libros."""
    print("\n" + "="*60)
    print(" TEST: Búsqueda de Libros")
    print("="*60)
    
    biblioteca = SistemaBiblioteca()
    biblioteca.agregar_libro("9780134685991", "Effective Python", "Brett Slatkin", 2019, "Programación", 1)
    biblioteca.agregar_libro("9781449355739", "Fluent Python", "Luciano Ramalho", 2015, "Programación", 2)
    
    # Búsqueda por título
    r = biblioteca.buscar_libros(criterio="titulo", valor="Effective")
    assert len(r) == 1
    print("✓ PASÓ: Búsqueda por título correcta.")
    
    # Búsqueda por autor
    r = biblioteca.buscar_libros(criterio="autor", valor="Ramalho")
    assert len(r) == 1
    print("✓ PASÓ: Búsqueda por autor correcta.")
    
    # Filtro por categoría
    r = biblioteca.buscar_libros(criterio="categoria", valor="Programación")
    assert len(r) == 2
    print("✓ PASÓ: Filtro por categoría correcto.")
    
    # Búsqueda sin resultados
    r = biblioteca.buscar_libros(criterio="titulo", valor="JavaScript")
    assert r == []
    print("✓ PASÓ: Manejo correcto de búsqueda sin resultados.")
    
    print("✓ Prueba completada")


def prueba_estadisticas():
    """Prueba generación de estadísticas."""
    print("\n" + "="*60)
    print(" TEST: Estadísticas")
    print("="*60)
    
    biblioteca = SistemaBiblioteca()
    biblioteca.agregar_libro("9780134685991", "Effective Python", "Brett Slatkin", 2019, "Programación", 2)
    biblioteca.registrar_usuario("U001", "Ana Pérez", "ana@correo.com")
    biblioteca.prestar_libro("9780134685991", "U001")
    
    top_libros = biblioteca.libros_mas_prestados()
    assert isinstance(top_libros, list)
    
    estad_categoria = biblioteca.estadisticas_categoria("Programación")
    assert isinstance(estad_categoria, dict)
    
    reporte = biblioteca.reporte_financiero()
    assert isinstance(reporte, dict)
    print("✓ PASÓ: Estadísticas generadas correctamente.")
    
    print("✓ Prueba completada")


def prueba_excepciones():
    """Prueba manejo de excepciones personalizadas."""
    print("\n" + "="*60)
    print(" TEST: Excepciones Personalizadas")
    print("="*60)
    
    biblioteca = SistemaBiblioteca()
    biblioteca.agregar_libro("9780134685991", "Effective Python", "Brett Slatkin", 2019, "Programación", 1)
    biblioteca.registrar_usuario("U001", "Ana Pérez", "ana@correo.com")
    
    # Libro no encontrado
    try:
        biblioteca.prestar_libro("9999999999999", "U001")
    except LibroNoEncontrado:
        print("✓ PASÓ: LibroNoEncontrado detectado correctamente.")
    
    # Usuario no registrado
    try:
        biblioteca.prestar_libro("9780134685991", "U999")
    except UsuarioNoRegistrado:
        print("✓ PASÓ: UsuarioNoRegistrado detectado correctamente.")
    
    print("✓ Prueba completada")


def prueba_importar_exportar():
    """Prueba importar/exportar catálogo."""
    print("\n" + "="*60)
    print(" TEST: Importar/Exportar")
    print("="*60)
    
    biblioteca = SistemaBiblioteca()
    
    # Agregar algunos libros antes de exportar
    biblioteca.agregar_libro("9780134685999", "Effective Python", "Brett Slatkin", 2019, "Programación", 3)
    biblioteca.agregar_libro("9580135404676", "Python Crash Course", "Eric Matthes", 2019, "Programación", 2)
    biblioteca.agregar_libro("9781449355732", "Fluent Python", "Luciano Ramalho", 2015, "Programación", 1)
    
    # Exportar el catálogo oficial
    archivo_exportado = "catalogo_biblioteca.txt"
    biblioteca.exportar_catalogo(archivo_exportado)
    print(f"✓ PASÓ: Catálogo exportado correctamente a '{archivo_exportado}'.")
    
    # Crear una nueva instancia vacía para probar la importación
    nueva_biblioteca = SistemaBiblioteca()
    
    resultado_import = nueva_biblioteca.importar_catalogo(archivo_exportado)
    assert isinstance(resultado_import, dict)
    
    # Verificar que los libros fueron cargados correctamente
    assert "9780134685991" in nueva_biblioteca.catalogo
    assert "9780135404676" in nueva_biblioteca.catalogo
    assert "9781449355739" in nueva_biblioteca.catalogo
    print("✓ PASÓ: Catálogo importado correctamente desde archivo.")
    
    # Intentar importar de nuevo (para probar manejo de duplicados)
    resultado_duplicado = nueva_biblioteca.importar_catalogo(archivo_exportado)
    errores = resultado_duplicado.get("errores", [])
    assert any("ya existe" in e[1] for e in errores)
    print("✓ PASÓ: Manejo correcto de duplicados durante importación.")
    
    print("✓ Prueba completada")


def prueba_renovar_prestamo():
    """Prueba renovación de préstamos."""
    print("\n" + "="*60)
    print(" TEST: Renovación de Préstamos")
    print("="*60)
    
    biblioteca = SistemaBiblioteca()
    biblioteca.agregar_libro("9780134685991", "Effective Python", "Brett Slatkin", 2019, "Programación", 1)
    biblioteca.registrar_usuario("U001", "Ana Pérez", "ana@correo.com")
    id_p = biblioteca.prestar_libro("9780134685991", "U001")
    
    biblioteca.renovar_prestamo(id_p)
    print("✓ PASÓ: Renovación de préstamo válida.")
    
    print("✓ Prueba completada")


def prueba_reporte_financiero():
    """Prueba reporte financiero."""
    print("\n" + "="*60)
    print(" TEST: Reporte Financiero")
    print("="*60)
    
    biblioteca = SistemaBiblioteca(multa_por_dia=2.0)
    biblioteca.agregar_libro("9780134685991", "Effective Python", "Brett Slatkin", 2019, "Programación", 1)
    biblioteca.registrar_usuario("U001", "Ana Pérez", "ana@correo.com")
    id_p = biblioteca.prestar_libro("9780134685991", "U001")
    
    biblioteca.prestamos[id_p]['fecha_vencimiento'] = datetime.now() - timedelta(days=2)
    biblioteca.devolver_libro(id_p)
    
    reporte = biblioteca.reporte_financiero()
    assert isinstance(reporte, dict)
    print("✓ PASÓ: Reporte financiero con multas generado correctamente.")
    
    print("✓ Prueba completada")


# ===========================================================================
# EJECUTAR TODAS LAS PRUEBAS
# ===========================================================================
def ejecutar_todas_las_pruebas():
    """Ejecuta todas las pruebas del sistema."""
    print("\n" + "="*70)
    print(" EJECUTANDO SUITE COMPLETA DE PRUEBAS")
    print("="*70)
    
    pruebas = [
        prueba_agregar_libros,
        prueba_registrar_usuarios,
        prueba_prestar_libros,
        prueba_devolver_libros,
        prueba_buscar_libros,
        prueba_estadisticas,
        prueba_excepciones,
        prueba_importar_exportar,
        prueba_renovar_prestamo,
        prueba_reporte_financiero
    ]
    
    exitosas = 0
    fallidas = 0
    
    for prueba in pruebas:
        try:
            prueba()
            exitosas += 1
        except Exception as e:
            print(f"✗ Error en {prueba.__name__}: {e}")
            fallidas += 1
    
    print("\n" + "="*70)
    print(" RESUMEN DE PRUEBAS")
    print("="*70)
    print(f"✓ Exitosas: {exitosas}/{len(pruebas)}")
    print(f"✗ Fallidas: {fallidas}/{len(pruebas)}")
    print("="*70)


if __name__ == "__main__":
    ejecutar_todas_las_pruebas()
