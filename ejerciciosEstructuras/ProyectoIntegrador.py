# Estephany Ruales Mazo
# PRoyecto Integrador

from collections import defaultdict
from datetime import datetime
import statistics

class AnalizadorVentas:
    def __init__(self, datos_ventas):
        self.ventas = datos_ventas
        self.ventas_por_categoria = self._agrupar_por("categoria")
        self.ventas_por_mes = self._agrupar_por_mes()
        self.ventas_por_vendedor = self._agrupar_por("vendedor")
        self.productos_vendidos = self._contar_productos()
    def _agrupar_por(self, campo):
        resultado = defaultdict(list)
        for v in self.ventas:
            resultado[v[campo]].append(v)
        return dict(resultado)
    def _agrupar_por_mes(self):
        resultado = defaultdict(list)
        for v in self.ventas:
            fecha = datetime.strptime(v["fecha"], "%Y-%m-%d")
            mes = f"{fecha.year}-{fecha.month:02d}"
            resultado[mes].append(v)
        return dict(resultado)
    def _contar_productos(self):
        c = {}
        for v in self.ventas:
            p = v["producto"]
            c[p] = c.get(p, 0) + 1
        return c
    def productos_mas_vendidos(self, n=3):
        return sorted(self.productos_vendidos.items(), key=lambda x: x[1], reverse=True)[:n]
    def total_ventas_por_categoria(self):
        return {cat: sum(v["precio"] for v in ventas) for cat, ventas in self.ventas_por_categoria.items()}
    def estadisticas_vendedor(self, vendedor):
        ventas = self.ventas_por_vendedor.get(vendedor)
        if not ventas:
            return None
        precios = [v["precio"] for v in ventas]
        return {
            "total": sum(precios),
            "promedio": statistics.mean(precios),
            "mediana": statistics.median(precios),
            "cantidad": len(precios),
            "min": min(precios),
            "max": max(precios)
        }
    def buscar_ventas(self, **criterios):
        resultado = []
        for v in self.ventas:
            cumple = True
            for campo, valor in criterios.items():
                if campo not in v or v[campo] != valor:
                    cumple = False; break
            if cumple:
                resultado.append(v)
        return resultado
    def buscar_por_rango_fechas(self, fecha_inicio, fecha_fin):
        fi = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        ff = datetime.strptime(fecha_fin, "%Y-%m-%d")
        return [v for v in self.ventas if fi <= datetime.strptime(v["fecha"], "%Y-%m-%d") <= ff]

if __name__ == "__main__":
    ventas = [
        {"id":1,"producto":"Laptop","categoria":"Electrónica","precio":1200,"fecha":"2023-01-15","vendedor":"Ana"},
        {"id":2,"producto":"Monitor","categoria":"Electrónica","precio":200,"fecha":"2023-01-20","vendedor":"Juan"},
        {"id":3,"producto":"Teclado","categoria":"Accesorios","precio":80,"fecha":"2023-02-05","vendedor":"Ana"},
        {"id":4,"producto":"Mouse","categoria":"Accesorios","precio":25,"fecha":"2023-02-10","vendedor":"Pedro"},
        {"id":5,"producto":"Laptop","categoria":"Electrónica","precio":1500,"fecha":"2023-02-15","vendedor":"Juan"},
        {"id":6,"producto":"Teléfono","categoria":"Electrónica","precio":800,"fecha":"2023-03-05","vendedor":"Ana"},
        {"id":7,"producto":"Tablet","categoria":"Electrónica","precio":300,"fecha":"2023-03-10","vendedor":"Pedro"},
        {"id":8,"producto":"Teclado","categoria":"Accesorios","precio":85,"fecha":"2023-03-15","vendedor":"Juan"},
        {"id":9,"producto":"Monitor","categoria":"Electrónica","precio":250,"fecha":"2023-04-05","vendedor":"Ana"},
        {"id":10,"producto":"Mouse","categoria":"Accesorios","precio":30,"fecha":"2023-04-10","vendedor":"Pedro"}
    ]
    analizador = AnalizadorVentas(ventas)
    print("Productos top 2:", analizador.productos_mas_vendidos(2))
    print("Total por categoría:", analizador.total_ventas_por_categoria())
    print("Estadísticas Ana:", analizador.estadisticas_vendedor("Ana"))
    print("Buscar accesorios vendidos por Juan:", analizador.buscar_ventas(categoria="Accesorios", vendedor="Juan"))
    print("Buscar por rango:", analizador.buscar_por_rango_fechas("2023-02-01","2023-03-31"))
