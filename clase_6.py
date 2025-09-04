from abc import ABC, abstractmethod
class Vehiculo(ABC):
    def __init__(self, marca:str,modelo:str,tipo:str,kilometraje:int, anio:int):
        self._marca = marca
        self._modelo = modelo
        self._tipo = tipo
        self._kilometraje = kilometraje
        self._anio = anio
        self._encendido = False
    # Metodo que se inicializa mas no se llena
    @abstractmethod
    def tipo_vehiculo(self) -> str:
        pass
    def encender(self):
        if not self._encendido:
            self._encendido = True
            print(f"Tu carro {self._marca} está encendido")
        else:
            print(f"Tu carro ya está encendido")
    def apagar(self):
        if self._encendido:
            self._encendido = False
            print(f"Tu carro {self._marca} está apagado")
        else:
            print(f"Tu carro ya está apagado")

    def obtener_informacion(self)->str:
        return (f"Vehiculo {self._marca}\n"
                f"Modelo {self._modelo}\n"
                f"Tipo {self._tipo}\n"
                f"Kilometraje {self._kilometraje}\n"
                f"Año {self._anio}\n")
    
    
class Motocicleta(Vehiculo):
    def __init__(self, marca:str, modelo:str, tipo:str, kilometraje:int, anio:int, cilindraje:int):
        super().__init__(marca, modelo, tipo, kilometraje, anio)
        self._cilindraje = cilindraje
    def tipo_vehiculo(self):
        print(f"La subclase es de tipo {self.tipo} ")
    def obtener_informacion(self):
        return (f"{super().obtener_informacion()}\n"
                f"Cilindraje {self._cilindraje} CC\n")


auto = Vehiculo("Marca", "2025", "SUV", 10000, 2024)
moto = Motocicleta("Yamaha", "2000", "Enduro", 13000,1999,600)
print(auto.obtener_informacion())
print(moto.obtener_informacion())