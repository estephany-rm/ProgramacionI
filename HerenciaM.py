class Animal:
    def comer(self):
        print("comer")
class Mamifero:
    def amamantar(self):
        print("amamntar")
class Ave:
    def volar(self):
        print("volar")

class Murcielago(Mamifero,Ave):
    pass
