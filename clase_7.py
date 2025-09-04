from abc import ABC, abstractmethod
from typing import List

class Empleado: 
    def __init__(self, nombre:str, edad:int, puesto:str):
        self.__nombre = nombre
        self.__edad = edad
        self.__puesto = puesto
    def get_nombre(self)->str:
        return self.__nombre
    def set_nombre(self, nombre:str)->None:
        self.__nombre = nombre
    def get_edad(self)->str:
        return self.__edad
    def set_edad(self, edad:str)->None:
        if edad > 0:
            self.__edad = edad
        else:
            print("Edad espera un valor entero mayor a 0")
    
    def get_puesto(self)->str:
        return self.__puesto
    def calcular_sueldo(self, horas_trabajas: float)-> float:
        return 0.0
    def __str__(self):
        return f"Name: {self.__nombre}, Edad: {self.__edad}, Puesto: {self.__puesto}"
    
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre:str, edad:int, puesto:str, hora_Sueldo:float):
        super().__init__(nombre, edad, puesto)
        self.__horaSueldo = hora_Sueldo
    def get_hora_sueldo(self)->float:
        return self.__horaSueldo
    def set_hora_sueldo(self, hora_sueldo:float)->None:
        if hora_sueldo > 0:
            self.__horaSueldo = hora_sueldo
        else:
            print("El valor por hora debe ser mayor a 0")
    def calcular_sueldo(self, horas_trabajas):
        if horas_trabajas <= 40:
            return horas_trabajas * self.__horaSueldo
        else:
            pagoRegular = self.__horaSueldo * 40
            PagoExtra = (horas_trabajas - 40) * (self.__horaSueldo *1.5)
            return pagoRegular + PagoExtra
    
    def __str__(self)->str:
        return f"{super().__str__()}, Valor Hora: {self.__horaSueldo:.2f}"

class EmpleadoMedioTiempo(Empleado):
    def __init__(self, nombre:str , edad:int , puesto:str, tarifa_hora:float):
        super().__init__(nombre, edad, puesto)
        self.__tarifa_hora = tarifa_hora
    def get_tarifa_hora(self)->float:
        return self.__tarifa_hora
    def set_tarifa_hora(self, tarifa_hora:float)->None:
        if tarifa_hora > 0:
            self.__horaSueldo = tarifa_hora
        else:
            print("La tarifa por hora debe ser mayor a 0")
    def calcular_sueldo(self, horas_trabajas:float)->float:
        return horas_trabajas * self.__tarifa_hora
    
    def __str__(self)->str:
        return f"{super().__str__()}, Valor Hora: {self.__tarifa_hora:.2f}"
    
class Departamento(ABC):
    @abstractmethod
    def agregar_empleado(self, empleado: Empleado)-> None:
        pass
    @abstractmethod
    def mostrar_empleados(self)->None:
        pass

class RecursosHumanos(Departamento):
    def __init__(self):
        self.__empleados: List(Empleado) = []
    def agregar_empleado(self, empleado):
        self.__empleados.append(empleado)
        print(f"El empleado {empleado.get_nombre()} se agrego al departamento de recursos humanos")
    def mostrar_empleados(self):
        print("Empleados del departamento de recursos humanos")
        for i, empleado in enumerate(self.__empleados,1):
            print(f"{i}. {empleado}")
    def calcular_nomina(self, horas_trabajas:dict)->float:
        total = 0.0
        for empleado in self.__empleados:
            horas = horas_trabajas.get(empleado.get_nombre(),0)
            sueldo = empleado.calcular_sueldo(horas)
            total += sueldo
            print(f"{empleado.get_nombre()}:{horas}, {sueldo:.2f}")
        return total

if __name__ == "__main__":
    # Crear empleados
    emp1 = EmpleadoTiempoCompleto("Carlos",30,"SD", 7.0)
    emp2 = EmpleadoTiempoCompleto("Maria",27,"PM", 15.0)
    emp3 = EmpleadoMedioTiempo("Gustavo",28,"Pr",5.0)
    emp4 = EmpleadoMedioTiempo("Gabriela",32,"Ds", 13.0)

    hr_dept = RecursosHumanos()
    hr_dept.agregar_empleado(emp1)
    hr_dept.agregar_empleado(emp2)
    hr_dept.agregar_empleado(emp3)
    hr_dept.agregar_empleado(emp4)
    print("\n", "-"*50)
    hr_dept.mostrar_empleados()
    horas_trabajadas = {
        "Carlos": 60,
        "Maria": 45,
        "Gustavo": 20,
        "Gabriela": 25
    }
    total_nomina = hr_dept.calcular_nomina(horas_trabajadas)
    print("\n", "-"*50)
    print(f"\n Total de la nomina es: {total_nomina:.2f}")