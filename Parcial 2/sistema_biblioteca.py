#!/usr/bin/env python3
"""
PARCIAL 2 - PROBLEMA INTEGRADOR (Parte 2)
Sistema de Gestión de Biblioteca Digital

Estudiante: Estephany Ruales Mazo
Fecha: 18/10/2025
"""
import os
from datetime import datetime, timedelta

# ===========================================================================
# EXCEPCIONES PERSONALIZADAS (5 puntos)
# ===========================================================================

class ErrorBiblioteca(Exception):
    """Excepción base para el sistema de biblioteca."""
    pass


class LibroNoEncontrado(ErrorBiblioteca):
    """Se lanza cuando un libro no existe en el catálogo."""
    def __init__(self, isbn):
        self.isbn = isbn
        super().__init__(f"Libro con ISBN {isbn} no encontrado")


class LibroNoDisponible(ErrorBiblioteca):
    """Se lanza cuando no hay copias disponibles."""
    def __init__(self, isbn, titulo):
        self.isbn = isbn
        self.titulo = titulo
        super().__init__(f"No hay copias disponibles de '{titulo}'")


class UsuarioNoRegistrado(ErrorBiblioteca):
    """Se lanza cuando el usuario no está registrado."""
    def __init__(self, id_usuario):
        self.id_usuario = id_usuario
        super().__init__(f"Usuario con ID '{id_usuario}' no está registrado")


class LimitePrestamosExcedido(ErrorBiblioteca):
    """Se lanza cuando el usuario excede el límite de préstamos."""
    def __init__(self, id_usuario, limite):
        self.id_usuario = id_usuario
        self.limite = limite
        super().__init__(f"Usuario {id_usuario} excede límite de {limite} préstamos")


class PrestamoVencido(ErrorBiblioteca):
    """Se lanza para operaciones con préstamos vencidos."""
    def __init__(self, id_prestamo, dias_retraso):
        self.id_prestamo = id_prestamo
        self.dias_retraso = dias_retraso
        super().__init__(f"Préstamo {id_prestamo} está vencido por {dias_retraso} días")

# ===========================================================================
# CLASE PRINCIPAL: SISTEMA BIBLIOTECA (35 puntos)
# ===========================================================================

class SistemaBiblioteca:
    """
    Sistema completo de gestión de biblioteca digital.
    """

    def __init__(self, dias_prestamo=14, multa_por_dia=1.0, limite_prestamos=3):
        self.catalogo = {}
        self.usuarios = {}
        self.prestamos = {}
        self.dias_prestamo = dias_prestamo
        self.multa_por_dia = multa_por_dia
        self.limite_prestamos = limite_prestamos
        self._contador_prestamos = 0

    # ===========================================================================
    # GESTIÓN DE CATÁLOGO
    # ===========================================================================

    def agregar_libro(self, isbn, titulo, autor, anio, categoria, copias):
        """
        Agrega un libro al catálogo.
        """        
        
        if not isinstance(isbn, str) or not isbn.isdigit() or len(isbn) != 13:
            raise ValueError("El ISBN debe ser un string de 13 dígitos numéricos.")
        if isbn in self.catalogo:
            raise KeyError(f"El ISBN {isbn} ya existe en el catálogo.")
        if not all(isinstance(s, str) and s for s in [titulo, autor, categoria]):
            raise ValueError("Título, autor y categoría no pueden ser vacíos.")
        if not isinstance(anio, int) or not (1000 <= anio <= datetime.now().year):
            raise ValueError(f"Año debe ser un entero entre 1000 y {datetime.now().year}.")
        if not isinstance(copias, int) or copias < 1:
            raise ValueError("El número de copias debe ser al menos 1.")

        self.catalogo[isbn] = {
            'titulo': titulo.strip(),
            'autor': autor.strip(),
            'anio': anio,
            'categoria': categoria.strip(),
            'copias_total': copias,
            'copias_disponibles': copias,
            'veces_prestado': 0
        }

    def actualizar_copias(self, isbn, cantidad_cambio):
        """
        Actualiza número de copias (añade o remueve).
        """
        
        if isbn not in self.catalogo:
            raise LibroNoEncontrado(isbn)

        libro = self.catalogo[isbn]
        nuevas_disp = libro['copias_disponibles'] + cantidad_cambio
        nuevas_total = libro['copias_total'] + cantidad_cambio
        if nuevas_disp < 0 or nuevas_total < 0:
            raise ValueError("El stock no puede ser negativo.")

        libro['copias_disponibles'] = nuevas_disp
        libro['copias_total'] = nuevas_total

    def buscar_libros(self, criterio='titulo', valor='', categoria=None):
        """Devuelve solo los campos solicitados en las aclaraciones."""
        resultados = []
        valor = str(valor).lower().strip()
        for isbn, libro in self.catalogo.items():
            if categoria and libro['categoria'].lower() != categoria.lower():
                continue
            if valor in str(libro.get(criterio, '')).lower():
                resultados.append({
                    'isbn': isbn,
                    'titulo': libro['titulo'],
                    'autor': libro['autor'],
                    'anio': libro['anio'],
                    'categoria': libro['categoria'],
                    'copias_disponibles': libro['copias_disponibles']
                })
        return resultados

    # ===========================================================================
    # GESTIÓN DE USUARIOS
    # ===========================================================================
    
    def registrar_usuario(self, id_usuario, nombre, email):
        """
        Registra un nuevo usuario en el sistema.
        Valida duplicados y formato de email.
        """
        # Verificar duplicados
        if id_usuario in self.usuarios:
            raise ValueError(f"El ID de usuario '{id_usuario}' ya está registrado.")

        # Validar nombre
        if not nombre or not isinstance(nombre, str):
            raise ValueError("El nombre no puede estar vacío.")

        # Validar email con un criterio simple (supuesto del enunciado)
        # Supuesto: Si el email no tiene '@' o no hay '.' después de '@', se considera inválido.
        if '@' not in email or '.' not in email.split('@')[-1]:
            raise ValueError("Email inválido.")

        # Registrar usuario
        self.usuarios[id_usuario] = {
            'nombre': nombre,
            'email': email,
            'fecha_registro': datetime.now(),
            'prestamos_activos': [],
            'historial': [],
            'multas_pendientes': 0.0
        }

        return f"Usuario '{nombre}' registrado correctamente."


    def obtener_estado_usuario(self, id_usuario):
        """
        Obtiene estado completo del usuario.
        """
        if id_usuario not in self.usuarios:
            raise UsuarioNoRegistrado(id_usuario)
        u = self.usuarios[id_usuario]
        puede_prestar = len(u['prestamos_activos']) < self.limite_prestamos and u['multas_pendientes'] <= 50
        return {
            'nombre': u['nombre'],
            'prestamos_activos': u['prestamos_activos'],
            'puede_prestar': puede_prestar,
            'multas_pendientes': u['multas_pendientes']
        }

    # ===========================================================================
    # GESTIÓN DE PRÉSTAMOS
    # ===========================================================================

    def prestar_libro(self, isbn, id_usuario):
        """
        Realiza un préstamo a un usuario, retorna un id unico del prestamo
        """
        if id_usuario not in self.usuarios:
            raise UsuarioNoRegistrado(id_usuario)
        if isbn not in self.catalogo:
            raise LibroNoEncontrado(isbn)

        u = self.usuarios[id_usuario]
        l = self.catalogo[isbn]

        if len(u['prestamos_activos']) >= self.limite_prestamos:
            raise LimitePrestamosExcedido(id_usuario, self.limite_prestamos)
        if l['copias_disponibles'] < 1:
            raise LibroNoDisponible(isbn, l['titulo'])
        if u['multas_pendientes'] > 50:
            raise ValueError(f"Usuario {id_usuario} tiene multas pendientes > $50.")

        self._contador_prestamos += 1
        id_prestamo = f"P{self._contador_prestamos:06d}"

        fecha_prestamo = datetime.now()
        fecha_vencimiento = fecha_prestamo + timedelta(days=self.dias_prestamo)

        self.prestamos[id_prestamo] = {
            'isbn': isbn,
            'id_usuario': id_usuario,
            'fecha_prestamo': fecha_prestamo,
            'fecha_vencimiento': fecha_vencimiento,
            'fecha_devolucion': None,
            'multa': 0.0
        }

        l['copias_disponibles'] -= 1
        l['veces_prestado'] += 1
        u['prestamos_activos'].append(id_prestamo)

        return id_prestamo
    

    def devolver_libro(self, id_prestamo):
        """
        Procesa devolución de libro.
        
        Calcula multa si hay retraso.
        Actualiza estado de libro y usuario.
        
        Returns:
            dict: {'dias_retraso': int, 'multa': float, 'mensaje': str}
        
        Raises:
            KeyError: Si préstamo no existe
            ValueError: Si ya fue devuelto
        """
        if id_prestamo not in self.prestamos:
            raise KeyError(f"El préstamo con ID {id_prestamo} no existe.")
        
        prestamo = self.prestamos[id_prestamo]
        
        if prestamo['fecha_devolucion'] is not None:
            raise ValueError(f"El préstamo {id_prestamo} ya fue devuelto.")
            
        # Calcular retraso y multa
        hoy = datetime.now()
        retraso = hoy - prestamo['fecha_vencimiento']
        dias_retraso = max(0, retraso.days)
        multa_calculada = dias_retraso * self.multa_por_dia
        
        # Actualizar estado del préstamo
        prestamo['fecha_devolucion'] = hoy
        prestamo['multa'] = multa_calculada
        
        # Actualizar copias disponibles del libro
        isbn = prestamo['isbn']
        if isbn in self.catalogo:
            self.catalogo[isbn]['copias_disponibles'] += 1
    
        # Actualizar el estado del usuario para reflejar la devolución
        id_usuario = prestamo['id_usuario']
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if id_prestamo in usuario['prestamos_activos']:
                usuario['prestamos_activos'].remove(id_prestamo)
            usuario['historial'].append(id_prestamo)
            usuario['multas_pendientes'] += multa_calculada
        
        # Crear mensaje de resultado
        if dias_retraso > 0:
            mensaje = f"Devolución con retraso de {dias_retraso} días. Multa: ${multa_calculada:.2f}"
        else:
            mensaje = "Libro devuelto a tiempo. Sin multa."
            
        return {
            'dias_retraso': dias_retraso,
            'multa': multa_calculada,
            'mensaje': mensaje
        }

    def renovar_prestamo(self, id_prestamo):
        """
        Renueva préstamo por otros N días (si no está vencido).
        """
        if id_prestamo not in self.prestamos:
            raise KeyError(f"El préstamo '{id_prestamo}' no existe.")
        p = self.prestamos[id_prestamo]
        hoy = datetime.now()
        if p['fecha_vencimiento'] < hoy:
            dias_retraso = (hoy - p['fecha_vencimiento']).days
            raise PrestamoVencido(id_prestamo, dias_retraso)

        p['fecha_vencimiento'] += timedelta(days=self.dias_prestamo)

    # ===========================================================================
    # ESTADÍSTICAS Y REPORTES
    # ===========================================================================

    def libros_mas_prestados(self, n=10):
        """
        Retorna los N libros más prestados.
        """
        libros_ordenados = sorted(
            self.catalogo.items(),
            key=lambda x: x[1]['veces_prestado'],
            reverse=True
        )
        return [(isbn, l['titulo'], l['veces_prestado']) for isbn, l in libros_ordenados[:n]]
 
    def usuarios_mas_activos(self, n=5):
        """
        Retorna los N usuarios más activos (más préstamos históricos).
        """
        ranking = sorted(
            self.usuarios.items(),
            key=lambda x: len(x[1]['historial']),
            reverse=True
        )
        return [(uid, u['nombre'], len(u['historial'])) for uid, u in ranking[:n]]

    def estadisticas_categoria(self, categoria):
        """
            Genera estadísticas de una categoría.
        """
        libros_cat = [l for l in self.catalogo.values() if l['categoria'].lower() == categoria.lower()]
        if not libros_cat:
            return {}
        total_libros = len(libros_cat)
        total_copias = sum(l['copias_total'] for l in libros_cat)
        copias_prestadas = sum(l['copias_total'] - l['copias_disponibles'] for l in libros_cat)
        tasa_prestamo = (copias_prestadas / total_copias) * 100
        libro_mas_popular = max(libros_cat, key=lambda l: l['veces_prestado'])['titulo']
        return {
            'total_libros': total_libros,
            'total_copias': total_copias,
            'copias_prestadas': copias_prestadas,
            'tasa_prestamo': round(tasa_prestamo, 2),
            'libro_mas_popular': libro_mas_popular
        }

    def prestamos_vencidos(self):
        """
        Lista préstamos actualmente vencidos.
        """
        hoy = datetime.now()
        vencidos = []
        for pid, p in self.prestamos.items():
            if p['fecha_devolucion'] is None and p['fecha_vencimiento'] < hoy:
                dias_retraso = (hoy - p['fecha_vencimiento']).days
                multa = dias_retraso * self.multa_por_dia
                titulo = self.catalogo[p['isbn']]['titulo']
                vencidos.append({
                    'id_prestamo': pid,
                    'isbn': p['isbn'],
                    'titulo': titulo,
                    'id_usuario': p['id_usuario'],
                    'dias_retraso': dias_retraso,
                    'multa_acumulada': multa
                })
        return vencidos
    
    def reporte_financiero(self, fecha_inicio=None, fecha_fin=None):
        """
        Genera reporte financiero de multas.
        """
        prestamos_a_considerar = []
        for p in self.prestamos.values():
            if p['fecha_devolucion'] is not None:
                en_rango = True
                if fecha_inicio and p['fecha_devolucion'] < fecha_inicio:
                    en_rango = False
                if fecha_fin and p['fecha_devolucion'] > fecha_fin:
                    en_rango = False
                if en_rango:
                    prestamos_a_considerar.append(p)

        multas_pagadas = sum(p['multa'] for p in prestamos_a_considerar)
    
        multas_pendientes = sum(u['multas_pendientes'] for u in self.usuarios.values())
        
        total_multas = multas_pagadas + multas_pendientes

        prestamos_con_multa = [p for p in prestamos_a_considerar if p['multa'] > 0]
        promedio_multa = (sum(p['multa'] for p in prestamos_con_multa) / len(prestamos_con_multa)) if prestamos_con_multa else 0

        return {
            'total_multas': round(total_multas, 2),
            'multas_pagadas': round(multas_pagadas, 2),
            'multas_pendientes': round(multas_pendientes, 2),
            'prestamos_con_multa': len(prestamos_con_multa),
            'promedio_multa': round(promedio_multa, 2)
        }

    # ===========================================================================
    # UTILIDADES
    # ===========================================================================

    def exportar_catalogo(self, archivo='catalogo_biblioteca.txt'):
        """
        Exporta catálogo a archivo de texto.
        Formato: ISBN|Título|Autor|Año|Categoría|Copias
        
        Maneja excepciones de archivo apropiadamente.
        """
        directorio_script = os.path.dirname(os.path.abspath(__file__))
        ruta_completa = os.path.join(directorio_script, archivo)
        
        # Primero, leer los ISBNs que ya existen en el archivo para no duplicarlos.
        isbns_en_archivo = set()
        try:
            with open(ruta_completa, 'r', encoding='utf-8') as f:
                for linea in f:
                    if '|' in linea:
                        isbns_en_archivo.add(linea.split('|')[0])
        except FileNotFoundError:
            pass  # Si el archivo no existe, el set simplemente quedará vacío.

        try:
            # Abrir en modo 'append' para añadir al final del archivo.
            with open(ruta_completa, 'a', encoding='utf-8') as f:
                for isbn, l in self.catalogo.items():
                    # Solo escribir el libro si su ISBN no está ya en el archivo.
                    if isbn not in isbns_en_archivo:
                        f.write(f"{isbn}|{l['titulo']}|{l['autor']}|{l['anio']}|{l['categoria']}|{l['copias_total']}\n")
            return True
        except Exception as e:
            print(f"Error exportando catálogo: {e}")
            return False

    def importar_catalogo(self, archivo='catalogo_biblioteca.txt'):
        """
        Importa catálogo desde archivo de texto.
        """
        directorio_script = os.path.dirname(os.path.abspath(__file__))
        ruta_completa = os.path.join(directorio_script, archivo)
        resultado = {'exitosos': 0, 'errores': []}
        try:
            with open(ruta_completa, 'r', encoding='utf-8') as f:
                for i, linea in enumerate(f, 1):
                    partes = linea.strip().split('|')
                    if len(partes) != 6:
                        resultado['errores'].append((i, "Formato de línea incorrecto (se esperaban 6 campos)."))
                        continue
                    isbn, titulo, autor, anio, categoria, copias = partes
                    if isbn in self.catalogo:
                        resultado['errores'].append((i, f"ISBN {isbn} ya existe (saltado)"))
                        continue
                    try:
                        self.agregar_libro(isbn, titulo, autor, int(anio), categoria, int(copias))
                        resultado['exitosos'] += 1
                    except Exception as e:
                        resultado['errores'].append((i, str(e)))
        except FileNotFoundError:
            resultado['errores'].append((0, f"El archivo '{ruta_completa}' no fue encontrado."))
        return resultado
