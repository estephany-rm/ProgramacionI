# Sistema de Gestión de Biblioteca
# Maria Paulina Paez Guzman 
# Estephany Ruales Mazo
from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class MaterialBiblioteca(ABC):
    def __init__(self, idMaterial:int, titulo:str, autor:str):
        self.__idMaterial = idMaterial
        self.__titulo = titulo
        self.__autor = autor
        self.__estaDisponible = True
    
    def get_idMaterial(self):
        return self.__idMaterial
    
    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor
    
    def get_estaDisponible(self):
        return self.__estaDisponible

    def set_id_material(self, id_material:int):
        self.__idMaterial = id_material

    def set_titulo(self, titulo:str):
        self.__titulo = titulo

    def set_autor(self,autor:str):
        self.__autor = autor
    
    def set_estaDisponible(self, newEstado: bool):
        self.__estaDisponible = newEstado
        
    @abstractmethod
    def calcular_fecha_devolucion(self, fechaPrestamo:datetime) -> datetime:
        pass
    @abstractmethod
    def obtener_tipo(self):
        pass
    @abstractmethod
    def obtener_detalles(self):
        pass


class Libro(MaterialBiblioteca):
    def __init__(self, idMaterial:int, titulo:str, autor:str,genero:str):
        super().__init__(idMaterial, titulo, autor)
        self.__genero = genero

    def get_genero(self)->str:
        return self.__genero
    
    def set_genero(self, newGenero:str):
        self.__genero = newGenero

    def calcular_fecha_devolucion(self, fechaPrestamo:datetime)->datetime:
        return fechaPrestamo + timedelta(days=15)
    
    def obtener_tipo(self)->str:
        return "Libro"
    
    def obtener_detalles(self)->str:
        return (f"Material Biblioteca: Libro \n"
                f"Titulo: {self.get_titulo()} \n"
                f"Id: {self.get_idMaterial()} \n"
                f"Autor: {self.get_autor()} \n"
                f"Género: {self.__genero} \n")

class Revista(MaterialBiblioteca):
    def __init__(self, idMaterial: int, titulo:str, autor:str, numero_edicion:int):
        super().__init__(idMaterial, titulo, autor)
        self.__numero_edicion = numero_edicion
    
    def get_numero_edicion(self)->int:
        return self.__numero_edicion
    
    def set_numero_edicion(self, newNumEdi: int):
        self.__numero_edicion = newNumEdi
    
    def calcular_fecha_devolucion(self, fechaPrestamo:datetime)->datetime:
        return fechaPrestamo + timedelta(days=7)
    
    def obtener_tipo(self)->str:
        return "Revista"
    
    def obtener_detalles(self)->str:
        return (f"Material Biblioteca: Revista \n"
                f"Titulo: {self.get_titulo()} \n"
                f"Id: {self.get_idMaterial()} \n"
                f"Autor: {self.get_autor()} \n"
                f"Numero de Edición: {self.__numero_edicion} \n")

class MaterialAudiovisual(MaterialBiblioteca):
    def __init__(self, idMaterial: int, titulo:str, autor:str,formato:str):
        super().__init__(idMaterial, titulo, autor)
        self.__formato = formato
    
    def get_formato(self)->str:
        return self.__formato
    
    def set_formato(self, newFormato: str):
        self.__formato = newFormato

    def calcular_fecha_devolucion(self, fechaPrestamo:datetime)->datetime:
        return fechaPrestamo + timedelta(days=3)
    
    def obtener_tipo(self)->str:
        return "Material Audiovisual"
    
    def obtener_detalles(self)->str:
        return (f"Material Biblioteca: Material Audiovisual \n"
                f"Titulo: {self.get_titulo()} \n"
                f"Id: {self.get_idMaterial()} \n"
                f"Autor: {self.get_autor()} \n"
                f"Formato: {self.__formato} \n")
    
    
class Usuario():
    def __init__(self, nombre:str,apellido:str,id:int):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__id = id

    def get_nombre(self)->str:
        return self.__nombre

    def set_nombre(self, nombre : str):
        self.__nombre = nombre

    def get_apellido(self)->str:
        return self.__apellido

    def set_apellido(self, apellido:str):
        self.__apellido = apellido

    def get_id(self)->int:
        return self.__id

    def set_id(self, id):
        self.__id = id
       
    def __str__(self)->str:
        return f"Usuario: {self.__nombre}, Apellido:{self.__apellido}, Id: {self.__id} "

class Prestamo():
    def __init__(self, usuario:Usuario, material:MaterialBiblioteca, fecha_prestamo:datetime):
        self.__usuario = usuario
        self.__material = material
        self.__fecha_prestamo = fecha_prestamo
        self.__fecha_devolucion = material.calcular_fecha_devolucion(fecha_prestamo)
        self.__material.set_estaDisponible(False)
    
    def finalizar_prestamo(self):
        self.__material.set_estaDisponible(True)

    def get_detalles(self):
        return (f"{self.__usuario.get_nombre()} prestó {self.__material.obtener_tipo()} "
                f"'{self.__material.get_titulo()}' el {self.__fecha_prestamo.date()} "
                f"(devolver antes de {self.__fecha_devolucion.date()})")

        

# Instancias de clases para el sistema de gestion
# Creacion de usuarios
usuario1 = Usuario("Ana", "Pérez", 1)
usuario2 = Usuario("Luis", "Gómez", 2)

# Creacion de materiales
libro1 = Libro(101, "Cien Años de Soledad", "Gabriel García Márquez", "Realismo mágico")
revista1 = Revista(201, "National Geographic", "Varios", 350)
dvd1 = MaterialAudiovisual(301, "Inception", "Christopher Nolan", "DVD")

# Mostrar detalles de los materiales
print(libro1.obtener_detalles())
print(revista1.obtener_detalles())
print(dvd1.obtener_detalles())

# Creacion de préstamo 
# Fecha (Anio, Mes, Dia)
fecha_prestamo = datetime(2025, 8, 1)
prestamo1 = Prestamo(usuario1, libro1, fecha_prestamo)
print(prestamo1.get_detalles())

# Finalización del préstamo
prestamo1.finalizar_prestamo()
print(f"Estado del libro tras devolución: {libro1.get_estaDisponible()}")    