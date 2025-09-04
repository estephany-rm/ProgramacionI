class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    
    def imprimeGrado(self):
        print(f"Grado : {self.grado}")

Estepha = Estudiante("Estephany", 17, 4)
Estepha.presentarse()
Estepha.imprimeGrado()