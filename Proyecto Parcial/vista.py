import time
import sys


class Vista:
    def mostrar_mensaje(self, mensaje: str, delay: float = 1.0):
        for c in mensaje:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.05) 
    
    def validacionDato(self,mensaje:str)->bool:
        if mensaje.isalpha():
                return False
        else: 
            return True
    
    def pedir_opcion(self, mensaje: str, limite: int):
        while True:
            opcion = input(mensaje)
            valida = self.validacionDato(opcion)
            if not valida:
                print("Opción inválida. Intenta de nuevo.")
            else:
                opcion = int(opcion) - 1
                if 0 <= opcion < limite:
                    return opcion
                else:
                    print("Opción inválida. Intenta de nuevo.")

