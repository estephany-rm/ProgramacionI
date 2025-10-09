# Estephany Ruales Mazo
# Ejercicios Prácticos: Operadores Lógicos en Python

print("NIVEL 1: Básico (Operadores Fundamentales)")

# --- Ejercicio 1.1: Predice los Resultados ---
print("\n--- Ejercicio 1.1 ---")
print(True and False)   # Mi predicción: False
print(True or False)    # Mi predicción: True
print(not True)         # Mi predicción: False
print(not False)        # Mi predicción: True
# Resultado real: False, True, False, True
# Explicación: Aplicando las tablas de verdad. 'and' necesita que ambos sean True.
# 'or' necesita que al menos uno sea True. 'not' invierte el valor booleano.

# --- Ejercicio 1.2: Operadores Combinados ---
print("\n--- Ejercicio 1.2 ---")
a, b, c = True, False, True
print(a and b)  # Mi predicción: False
print(a or b)   # Mi predicción: True
print(b or c)   # Mi predicción: True
print(a and c)  # Mi predicción: True
# Resultado real: False, True, True, True
# Explicación: Se evalúan las expresiones reemplazando las variables por sus valores booleanos.

# --- Ejercicio 1.3: Precedencia ---
print("\n--- Ejercicio 1.3 ---")
a, b, c = True, False, True
print(a and b or c)      # Mi predicción: True
print(a or b and c)      # Mi predicción: True
print(not a or b)        # Mi predicción: False
print(not (a or b))      # Mi predicción: False
# Resultado real: True, True, False, False
# Explicación: El orden de precedencia es: 1. not, 2. and, 3. or.
# (a and b or c) -> (True and False) or True -> False or True -> True
# (not (a or b)) -> not (True or False) -> not True -> False

# --- Ejercicio 1.4: Comparaciones y Lógica ---
print("\n--- Ejercicio 1.4 ---")
x = 5
print(x > 3 and x < 10)  # Mi predicción: True
print(x < 3 or x > 10)   # Mi predicción: False
print(not x > 3)         # Mi predicción: False
# Resultado real: True, False, False
# Explicación: Las comparaciones (>, <) se resuelven primero, dando como resultado
# (True/False), que luego son evaluados por los operadores lógicos.

# --- Ejercicio 1.5: Comparaciones Encadenadas ---
print("\n--- Ejercicio 1.5 ---")
x = 5
print(3 < x < 10)        # Mi predicción: True
print(1 <= x <= 3)       # Mi predicción: False
print(10 > x > 3)        # Mi predicción: True
# Resultado real: True, False, True
# Explicación: Python permite encadenar comparaciones. 3 < x < 10 es una
# forma más corta y legible de escribir (3 < x) and (x < 10).

print("\nNIVEL 2: Intermedio (Valores y Cortocircuito)")

# --- Ejercicio 2.1: Valores Retornados ---
print("\n--- Ejercicio 2.1 ---")
print("hola" and "mundo")  # Mi predicción: "mundo"
print("hola" and "")       # Mi predicción: ""
print("" and "mundo")      # Mi predicción: ""
print("hola" or "mundo")   # Mi predicción: "hola"
print("" or "mundo")       # Mi predicción: "mundo"
# Resultado real: 'mundo', '', '', 'hola', 'mundo'
# Explicación: 'and' retorna el primer valor "falsy" que encuentra, o el último si todos son "truthy".
# 'or' retorna el primer valor "truthy" que encuentra, o el último si todos son "falsy".

# --- Ejercicio 2.2: Truthy y Falsy ---
print("\n--- Ejercicio 2.2 ---")
print(bool(0))          # Mi predicción: False
print(bool(""))         # Mi predicción: False
print(bool([]))         # Mi predicción: False
print(bool([0]))        # Mi predicción: True
print(bool(" "))        # Mi predicción: True
print(bool(None))       # Mi predicción: False
# Resultado real: False, False, False, True, True, False
# Explicación: En Python, ciertos valores se consideran "falsy": el número 0,
# contenedores vacíos (cadenas, listas, diccionarios) y None. Casi todo lo demás es "truthy".

# --- Ejercicio 2.3: Evaluación de Cortocircuito ---
print("\n--- Ejercicio 2.3 ---")
def f1():
    print("f1 ejecutada")
    return True

def f2():
    print("f2 ejecutada")
    return False

# Predicción: Se imprimirán "f1 ejecutada", "f2 ejecutada", y el resultado será False.
# Luego se imprimirá "f2 ejecutada" y el resultado será False.
# Finalmente se imprimirá "f1 ejecutada" y el resultado será True.
print("Caso 1 (f1() and f2()):")
f1() and f2()
print("\nCaso 2 (f2() and f1()):")
f2() and f1()
print("\nCaso 3 (f1() or f2()):")
f1() or f2()
# Resultado real: (ver la ejecución)
# Explicación: Con 'and', si el primer valor es False, Python no necesita evaluar el segundo (cortocircuito).
# Con 'or', si el primer valor es True, Python no evalúa el segundo (cortocircuito).

# --- Ejercicio 2.4: Operadores de Pertenencia ---
print("\n--- Ejercicio 2.4 ---")
nums = [1, 2, 3, 4, 5]
print(3 in nums)        # Mi predicción: True
print(6 in nums)        # Mi predicción: False
print(6 not in nums)    # Mi predicción: True

word = "Python"
print("P" in word)      # Mi predicción: True
print("p" in word)      # Mi predicción: False
print("th" in word)     # Mi predicción: True
# Resultado real: True, False, True, True, False, True
# Explicación: 'in' y 'not in' verifican si un elemento existe o no dentro de una secuencia (lista, cadena, etc.).
# La comparación en cadenas distingue entre mayúsculas y minúsculas.

# --- Ejercicio 2.5: Identidad vs Igualdad ---
print("\n--- Ejercicio 2.5 ---")
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

print(lista1 == lista2)  # Mi predicción: True
print(lista1 is lista2)  # Mi predicción: False
print(lista1 == lista3)  # Mi predicción: True
print(lista1 is lista3)  # Mi predicción: True
# Resultado real: True, False, True, True
# Explicación: '==' compara el contenido (valor) de los objetos. 'is' compara si son
# el mismo objeto en memoria (su identidad). lista1 y lista2 son dos objetos distintos
# con el mismo contenido, mientras que lista1 y lista3 apuntan al mismo objeto.

print("\nNIVEL 3 Y PROYECTO")

# --- Ejercicio 3.1: Validación de Formulario ---
print("\n--- Ejercicio 3.1 ---")
def validar_datos(nombre, email, edad, password):
    val_nombre = nombre and 2 <= len(nombre) <= 30
    val_email = email and '@' in email
    val_edad = edad and edad >= 18
    val_pass = password and len(password) >= 8
    return val_nombre and val_email and val_edad and val_pass

print(f"Prueba válida: {validar_datos('Ana', 'ana@email.com', 25, 'secreto123')}") # Predicción: True
print(f"Prueba inválida: {validar_datos('', 'no-email', 15, '123')}")      # Predicción: False

# --- Ejercicio 3.2: Sistema de Autorización ---
print("\n--- Ejercicio 3.2 ---")
def puede_acceder(usuario, permiso_requerido, lista_negra):
    return (usuario["autenticado"] and
            (usuario["admin"] or permiso_requerido in usuario["permisos"]) and
            usuario["id"] not in lista_negra)

# Datos de prueba
admin = {"id": 1, "autenticado": True, "admin": True, "permisos": ["leer", "escribir"]}
usuario_normal = {"id": 2, "autenticado": True, "admin": False, "permisos": ["leer"]}
usuario_bloqueado = {"id": 3, "autenticado": True, "admin": False, "permisos": ["leer", "escribir"]}
lista_negra_usuarios = [3, 4]

print(f'puede_acceder(admin, "borrar", lista_negra_usuarios) -> {puede_acceder(admin, "borrar", lista_negra_usuarios)}')
print(f'puede_acceder(usuario_normal, "leer", lista_negra_usuarios) -> {puede_acceder(usuario_normal, "leer", lista_negra_usuarios)}')
print(f'puede_acceder(usuario_normal, "escribir", lista_negra_usuarios) -> {puede_acceder(usuario_normal, "escribir", lista_negra_usuarios)}')
print(f'puede_acceder(usuario_bloqueado, "leer", lista_negra_usuarios) -> {puede_acceder(usuario_bloqueado, "leer", lista_negra_usuarios)}')

# --- Ejercicio 3.3: Acceso Seguro a Diccionario ---
print("\n--- Ejercicio 3.3 ---")
def obtener_valor_seguro(diccionario, clave, predeterminado=None):
    # Usando un operador ternario
    return diccionario[clave] if clave in diccionario else predeterminado

config = {"timeout": 30, "retries": 3}
print(f'obtener_valor_seguro(config, "timeout") -> {obtener_valor_seguro(config, "timeout")}')
print(f'obtener_valor_seguro(config, "cache") -> {obtener_valor_seguro(config, "cache")}')
print(f'obtener_valor_seguro(config, "cache", 60) -> {obtener_valor_seguro(config, "cache", 60)}')

# --- Ejercicio 3.4: Filtrar Lista (Ejemplo de implementación) ---
print("\n--- Ejercicio 3.4 ---")
def filtrar_productos(productos, precio_min, precio_max, categoria=None):
    filtrados = []
    for p in productos:
        cond_precio = precio_min <= p["precio"] <= precio_max
        cond_disponible = p["disponible"]
        cond_categoria = (categoria is None or p["categoria"] == categoria)
        
        if cond_precio and cond_disponible and cond_categoria:
            filtrados.append(p)
    return filtrados

productos = [
    {"nombre": "Laptop", "precio": 1200, "categoria": "Electrónica", "disponible": True},
    {"nombre": "Teléfono", "precio": 800, "categoria": "Electrónica", "disponible": False},
    {"nombre": "Libro", "precio": 15, "categoria": "Libros", "disponible": True},
    {"nombre": "Audífonos", "precio": 200, "categoria": "Electrónica", "disponible": True},
]
print(f"Filtro (0-500): {filtrar_productos(productos, 0, 500)}")

# --- Ejercicio 3.5: Evaluación de Riesgo ---
print("\n--- Ejercicio 3.5 ---")
def evaluar_riesgo(cliente):
    cond1 = cliente["score_crediticio"] > 700
    cond2 = cliente["ingreso_anual"] > 50000 and cliente["años_historial"] > 2
    cond3 = cliente["vip"] and not cliente["deudas_pendientes"]
    
    return cond1 or cond2 or cond3

cliente1 = {"nombre": "Ana García", "score_crediticio": 720, "ingreso_anual": 45000, "años_historial": 3, "vip": False, "deudas_pendientes": False}
cliente2 = {"nombre": "Luis Pérez", "score_crediticio": 680, "ingreso_anual": 60000, "años_historial": 4, "vip": False, "deudas_pendientes": False}
cliente3 = {"nombre": "Carmen Ruiz", "score_crediticio": 690, "ingreso_anual": 30000, "años_historial": 1, "vip": True, "deudas_pendientes": False}

print(f"Evaluar riesgo cliente 1 (Ana): {evaluar_riesgo(cliente1)}")
print(f"Evaluar riesgo cliente 2 (Luis): {evaluar_riesgo(cliente2)}") 
print(f"Evaluar riesgo cliente 3 (Carmen): {evaluar_riesgo(cliente3)}") 


print("\nPROYECTO FINAL: Sistema de Control de Acceso")
usuarios = [
    {"id": 1, "nombre": "Admin", "roles": ["admin"], "permisos": ["leer", "escribir", "eliminar"], "plan": "premium", "activo": True, "edad": 35},
    {"id": 2, "nombre": "Usuario Regular", "roles": ["usuario"], "permisos": ["leer"], "plan": "basico", "activo": True, "edad": 17},
    {"id": 3, "nombre": "Usuario Premium", "roles": ["usuario"], "permisos": ["leer", "escribir"], "plan": "premium", "activo": True, "edad": 25},
    {"id": 4, "nombre": "Usuario Inactivo", "roles": ["usuario"], "permisos": ["leer"], "plan": "basico", "activo": False, "edad": 40},
]
recursos = [
    {"id": 1, "nombre": "Panel Admin", "requiere_rol": ["admin"], "requiere_permiso": "eliminar", "solo_adultos": False},
    {"id": 2, "nombre": "Contenido Premium", "requiere_rol": ["usuario", "admin"], "requiere_permiso": "leer", "solo_premium": True},
    {"id": 3, "nombre": "Contenido para Adultos", "requiere_rol": ["usuario", "admin"], "requiere_permiso": "leer", "solo_adultos": True},
]

def puede_acceder_recurso(usuario, recurso):
    if not usuario["activo"]:
        return False, "Usuario inactivo"
    
    tiene_rol_requerido = any(rol in recurso.get("requiere_rol", []) for rol in usuario["roles"])
    if not tiene_rol_requerido:
        return False, f"Requiere uno de los roles: {recurso.get('requiere_rol')}"
    
    if "requiere_permiso" in recurso and recurso["requiere_permiso"] not in usuario["permisos"]:
        return False, f"Falta el permiso: {recurso['requiere_permiso']}"
    
    if recurso.get("solo_premium", False) and usuario["plan"] != "premium":
        return False, "Requiere plan premium"
    
    if recurso.get("solo_adultos", False) and usuario["edad"] < 18:
        return False, "Solo para mayores de 18 años"
    
    return True, "Acceso permitido"

def probar_accesos():
    for usuario in usuarios:
        print(f"\nProbando acceso para: {usuario['nombre']}")
        for recurso in recursos:
            acceso, motivo = puede_acceder_recurso(usuario, recurso)
            estado = "PERMITIDO" if acceso else "DENEGADO"
            print(f"Recurso: '{recurso['nombre']}' -> {estado} (Razón: {motivo})")
probar_accesos()


print("\nEjercicios de Debugging")

# --- Debug 1: Encuentra el Error ---
print("\n--- Debug 1 ---")
# Código erroneo:
# def verificar_permisos(usuario, accion):
#     if usuario["permisos"] and accion in usuario["permisos"]:
#         return True
#     else:
#         return False
# usuario = {"id": 1, "nombre": "Juan"}
# print(verificar_permisos(usuario, "leer"))
# ¿Qué está mal?: El código causa un KeyError porque intenta acceder a usuario["permisos"]
# en un diccionario donde esa clave no existe.

# Código corregido:
def verificar_permisos_corregido(usuario, accion):
    return "permisos" in usuario and accion in usuario["permisos"]

usuario_sin_permisos = {"id": 1, "nombre": "Juan"}
print(f"Permiso 'leer' para Juan: {verificar_permisos_corregido(usuario_sin_permisos, 'leer')}") # Predicción: False
# Explicación: Se usa "permisos" in usuario para verificar si la clave existe.
# Gracias al cortocircuito, si la clave no existe, la expresión da False y la segunda
# parte (que causaría el error) nunca se ejecuta.

# --- Debug 2: Encuentra el Error ---
print("\n--- Debug 2 ---")
# Código erroneo:
# estudiantes = [
#     {"nombre": "Ana", "nota": 85},
#     {"nombre": "Luis", "nota": None},
#     {"nombre": "Carmen", "nota": 92}
# ]
# aprobados = [e for e in estudiantes if e["nota"] >= 60]
# ¿Qué está mal?: El código causa un TypeError porque intenta comparar None >= 60 para el estudiante Luis.
# La comparación entre un NoneType y un entero no está permitida.

# Código corregido:
estudiantes = [
    {"nombre": "Ana", "nota": 85},
    {"nombre": "Luis", "nota": None},
    {"nombre": "Carmen", "nota": 92}
]
aprobados = [e for e in estudiantes if e["nota"] is not None and e["nota"] >= 60]
print(f"Aprobados (corregido): {aprobados}")
# Explicación de la corrección: Se añade 'e["nota"] is not None and ...'. Gracias
# al cortocircuito, si la nota es None, la primera parte es False y la segunda
# parte nunca se llega a ejecutar.

# ✅ Autoevaluación
# Marca los ejercicios que completaste correctamente:

# Nivel 1 (Básico)
# [O] Ejercicio 1.1
# [O] Ejercicio 1.2
# [O] Ejercicio 1.3
# [O] Ejercicio 1.4
# [O] Ejercicio 1.5
# Nivel 2 (Intermedio)
# [O] Ejercicio 2.1
# [O] Ejercicio 2.2
# [O] Ejercicio 2.3
# [O] Ejercicio 2.4
# [O] Ejercicio 2.5
# Nivel 3 (Avanzado)
# [O] Ejercicio 3.1
# [O] Ejercicio 3.2
# [O] Ejercicio 3.3
# [O] Ejercicio 3.4
# [O] Ejercicio 3.5
# Proyecto Final
# [O] Sistema de Control de Acceso