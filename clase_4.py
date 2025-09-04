# class Factura:
#     pass
#     # def __init__(self,fecha,total,vendedor):
#     #     self.fecha = fecha
#     #     self.total = total
#     #     self.vendedor = vendedor
#     # def __str__(self):
#     #     cadena = str()
#     #     cadena+= f" Fecha: {self.fecha}\n Total: {self.total}\n Vendedor: {self.vendedor}\n"
#     #     return cadena
# print(Factura())

class Player():
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.health = 100
    
    def move(self,dx, dy):
        self.x += dx
        self.y += dy
    
    def damage(self,pst):
        self.health -= pst