class CuentaBancaria:
    def __init__(self, balance):
        self.__balance = balance

    def deposito(self, cantidad):
        self.__balance += cantidad
    
    def retirar(self, cantidad):
        if self.__balance >= cantidad:
            self.__balance -= cantidad
        else:
            print("Fondos insuficientes")
    
    def mostrarBalance(self):
        return self.__balance

miCuenta = CuentaBancaria(200000)
miCuenta.deposito(570)
miCuenta.retirar(43000)
print(miCuenta.mostrarBalance())