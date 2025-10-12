# Estephany Ruales Mazo
# Ejercicios Practicos 2

from collections import defaultdict,OrderedDict
import json

# Nivel Básico
# Ejercicio B1: Filtrado de listas
def filtrar_pares(numeros):
    return [n for n in numeros if n % 2 == 0]

# Ejercicio B2: Invertir diccionario
def invertir_diccionario(diccionario):
    return {v: k for k, v in diccionario.items()}

# Ejercicio B3: Elementos comunes en dos listas
def elementos_comunes(lista1, lista2):
    return list(set(lista1) & set(lista2))

# Ejercicio B4: Contador de palabras
def contar_palabras(texto):
    palabras = texto.lower().split()
    contador = {}
    for p in palabras:
        contador[p] = contador.get(p, 0) + 1
    return contador

# Ejercicio B5: Eliminar duplicados manteniendo orden
def eliminar_duplicados(lista):
    return list(dict.fromkeys(lista))

# Nivel Intermedio
# Ejercicio I1: Agrupar por atributo
def agrupar_por(objetos, atributo):
    resultado = defaultdict(list)
    for obj in objetos:
        resultado[obj[atributo]].append(obj)
    return dict(resultado)

# Ejercicio I2: Fusionar diccionarios anidados
def fusionar_diccionarios(dict1, dict2):
    resultado = dict1.copy()
    for k, v in dict2.items():
        if k in resultado and isinstance(resultado[k], dict) and isinstance(v, dict):
            resultado[k] = fusionar_diccionarios(resultado[k], v)
        else:
            resultado[k] = v
    return resultado

# Ejercicio I3: Encontrar el par que suma
def encontrar_par_suma(numeros, objetivo):
    vistos = set()
    for num in numeros:
        comp = objetivo - num
        if comp in vistos:
            return (comp, num)
        vistos.add(num)
    return None

# Ejercicio I4: Matriz como lista de listas
def transponer(matriz):
    if not matriz:
        return []
    return [list(fila) for fila in zip(*matriz)]

# Ejercicio I5: Contar elementos únicos por categoría
def contar_por_categoria(datos):
    categorias = {}
    for categoria, elemento in datos:
        categorias.setdefault(categoria, set()).add(elemento)
    return {c: len(s) for c, s in categorias.items()}

# Nivel Avanzado
# Ejercicio A1: Memoización con diccionario
def fibonacci(n):
    memoria = {0:0, 1:1}
    def fib_m(n):
        if n in memoria:
            return memoria[n]
        memoria[n] = fib_m(n-1) + fib_m(n-2)
        return memoria[n]
    return fib_m(n)


# Ejercicio A2: Sistema de caché LRU
class LRUCache:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cache = OrderedDict()
    def get(self, clave):
        if clave not in self.cache:
            return None
        self.cache.move_to_end(clave)
        return self.cache[clave]
    def put(self, clave, valor):
        if clave in self.cache:
            self.cache.move_to_end(clave)
        self.cache[clave] = valor
        if len(self.cache) > self.capacidad:
            self.cache.popitem(last=False)

# Ejercicio A3: Implementar conjunto con lista
class MiConjunto:
    def __init__(self):
        self.elementos = []
    def add(self, elemento):
        if elemento not in self.elementos:
            self.elementos.append(elemento)
    def remove(self, elemento):
        if elemento in self.elementos:
            self.elementos.remove(elemento)
        else:
            raise KeyError(f"{elemento} no está en el conjunto")
    def discard(self, elemento):
        if elemento in self.elementos:
            self.elementos.remove(elemento)
    def __contains__(self, elemento):
        return elemento in self.elementos
    def __len__(self):
        return len(self.elementos)
    def __str__(self):
        return "{" + ", ".join(str(e) for e in self.elementos) + "}"

# Ejercicio A4: Filtrado de datos anidados
def filtrar_jugadores(datos, condicion):
    resultado = {}
    for equipo, info in datos.items():
        jugadores_filtrados = [j for j in info.get("jugadores", []) if condicion(j)]
        if jugadores_filtrados:
            resultado[equipo] = {"jugadores": jugadores_filtrados}
    return resultado

# Ejercicio A5: Operaciones sobre árboles (diccionarios anidados)
def encontrar_ruta(arbol, valor):
    def buscar(nodo, camino):
        if nodo is None:
            return None
        camino.append(nodo["valor"])
        if nodo["valor"] == valor:
            return camino
        izq = buscar(nodo.get("izquierdo"), camino.copy())
        if izq:
            return izq
        der = buscar(nodo.get("derecho"), camino.copy())
        if der:
            return der
        return None
    return buscar(arbol, [])

# Ejercicios de Depuración
# 🐞 Depuración 1: Modificación no intencionada
# Código con error:
# def agregar_puntos(equipos, equipo, puntos):
#     equipos[equipo] = puntos
#     return equipos

def agregar_puntos(equipos, equipo, puntos):
    resultado = equipos.copy()
    resultado[equipo] = puntos
    return resultado   

# 🐞 Depuración 2: Referencia circular en JSON
# Código con error:
# Crear estructura con referencia circular
class ReferenceResolver:
    def __init__(self):
        self.memo = {}
        self.counter = 0

    def __call__(self, obj):
        if isinstance(obj, dict):
            oid = id(obj)
            if oid in self.memo:
                return {"$ref": self.memo[oid]}
            self.counter += 1
            ref_id = f"id{self.counter}"
            self.memo[oid] = ref_id
            result = {"$id": ref_id}
            for k, v in obj.items():
                result[k] = self(v)
            return result
        return obj


# 🐞 Depuración 3: Modificación durante iteración
# Código con error:
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Eliminar números pares
# for numero in numeros:
#     if numero % 2 == 0:
#         numeros.remove(numero)

def eliminar_pares(numeros):
    return [x for x in numeros if x % 2 != 0]


if __name__ == "__main__":
    ejercicio1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ejercicio2 = {"a": 1, "b": 2, "c": 3}
    ejercicio31 = [1, 2, 3, 4, 5]
    ejercicio32 = [4, 5, 6, 7, 8]
    ejercicio4 = "hola mundo hola python"
    ejercicio5 = [1, 2, 2, 3, 4, 3, 5]
    print()
    print("--- Nivel Básico ---")
    print("="*50)
    print()
    print("filtrar_pares:", filtrar_pares(ejercicio1))
    print()
    print("invertir_diccionario:", invertir_diccionario(ejercicio2))
    print()
    print("elementos_comunes:", elementos_comunes(ejercicio31,ejercicio32))
    print()
    print("contar_palabras:", contar_palabras(ejercicio4))
    print()
    print("eliminar_duplicados:", eliminar_duplicados(ejercicio5))

    estudiantes = [
    {"nombre": "Ana", "ciudad": "Madrid"},
    {"nombre": "Juan", "ciudad": "Barcelona"},
    {"nombre": "Maria", "ciudad": "Madrid"},
    {"nombre": "Pedro", "ciudad": "Valencia"}
    ]
    dict1 = {"a": 1, "b": {"x": 10, "y": 20}}
    dict2 = {"c": 3, "b": {"y": 30, "z": 40}}

    datos = [
    ("fruta", "manzana"),
    ("verdura", "zanahoria"),
    ("fruta", "plátano"),
    ("fruta", "manzana"),
    ("verdura", "lechuga")
    ]
    print()
    print()
    print("--- Nivel Intermedio ---")
    print("="*50)
    print()
    print("agrupar_por:", agrupar_por(estudiantes, "ciudad"))
    print()
    print("fusionar_dic:", fusionar_diccionarios(dict1, dict2))
    print()
    print("encontrar_par_suma:", encontrar_par_suma([1,5,3,7,9,2], 10))
    print()
    print("transponer:", transponer([[1,2,3],[4,5,6], [7, 8, 9]]))
    print()
    print("contar_por_categoria:", contar_por_categoria(datos))
    
    print()
    print()
    print("--- Nivel Avanzado ---")
    print("="*50)
    print()
    print("fibonacci(10):", fibonacci(10))
    print()
    c = LRUCache(2)
    c.put(1,"uno"); c.put(2,"dos")
    print("LRU get 1:", c.get(1))
    c.put(3,"tres")
    print("LRU get 2 (debe ser None):", c.get(2))
    s = MiConjunto()
    s.add(1); s.add(2); s.add(1)
    
    print("MiConjunto len:", len(s), "contains 1:", 1 in s)

    datos = {
    "equipo1": {"jugadores": [{"nombre": "Ana", "puntos": 120}, {"nombre": "Juan", "puntos": 80}]},
    "equipo2": {"jugadores": [{"nombre": "Maria", "puntos": 90}, {"nombre": "Pedro", "puntos": 150}]}
    }
    print()
    print(filtrar_jugadores(datos, lambda j: j["puntos"] > 100))
    
    arbol = {
    "valor": "A",
    "izquierdo": {
        "valor": "B",
        "izquierdo": {"valor": "D", "izquierdo": None, "derecho": None},
        "derecho": {"valor": "E", "izquierdo": None, "derecho": None}
    },
    "derecho": {
        "valor": "C",
        "izquierdo": None,
        "derecho": {"valor": "F", "izquierdo": None, "derecho": None}
    }
    }
    print()
    print(encontrar_ruta(arbol, "F"))
    print()
    print("Ejercicios de Depuracion")
    print()
    print("Depuracion 1")
    print()
    puntuacion = {"Equipo A": 10, "Equipo B": 15}
    nuevos = agregar_puntos(puntuacion, "Equipo C", 12)
    print(puntuacion)  
    print(nuevos)  
    print()
    print("Depuracion 2")
    print()
    # Datos con referencia circular
    a = {"nombre": "objeto a"}
    b = {"nombre": "objeto b", "referencia": a}
    a["referencia"] = b
    resolver = ReferenceResolver()
    resolved = resolver(a)
    print("Serializado:\n", json.dumps(resolved, indent=2))

    print()
    print("Depuracion 3")
    print()
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("eliminar_pares:", eliminar_pares(numeros))
