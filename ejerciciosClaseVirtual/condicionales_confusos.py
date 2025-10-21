# Estephany Ruales Mazo
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar_enter(mensaje="Presiona Enter para continuar..."):
    try:
        input(f"\n{mensaje}")
    except EOFError:
        print()

def mostrar_titulo(texto):
    print("\n" + "=" * 70)
    print(texto.center(70))
    print("=" * 70 + "\n")

def mostrar_seccion(texto):
    print("\n" + "-" * 50)
    print(texto)
    print("-" * 50)

def main():
    limpiar_pantalla()
    mostrar_titulo("ESTRUCTURAS CONDICIONALES EN PYTHON - Sesión Interactiva (Resuelta)")

    print("¡Bienvenidos! Esta versión funciona en entornos interactivos y no interactivos.")
    esperar_enter()

    # EJERCICIO 1
    limpiar_pantalla()
    mostrar_titulo("EJERCICIO 1: INDENTACIÓN EN CONDICIONALES")
    print("Código de ejemplo y resultado con edad = 17:")
    edad = 17
    if edad < 18:
        print("Eres menor de edad")
        print("No puedes entrar")
    print("Verificación completada")
    esperar_enter()

    # EJERCICIO 2
    limpiar_pantalla()
    mostrar_titulo("EJERCICIO 2: ASIGNACIÓN VS COMPARACIÓN")
    print("El operador de comparación es '=='. Ejemplo corregido:")
    x = 5
    if x == 10:
        print("x es igual a 10")
    else:
        print("x no es igual a 10")
    esperar_enter()

    # EJERCICIO 3
    limpiar_pantalla()
    mostrar_titulo("EJERCICIO 3: VALORES COMO CONDICIONES")
    valores = [0, 1, "", "texto", [], [1, 2], None, True, False]
    for valor in valores:
        if valor:
            print(f"{repr(valor)} se evalúa como True")
        else:
            print(f"{repr(valor)} se evalúa como False")
    esperar_enter()

    # EJERCICIO 4
    limpiar_pantalla()
    mostrar_titulo("EJERCICIO 4: ANIDACIÓN DE CONDICIONALES")
    edad = 16
    tiene_permiso = True
    if edad < 18:
        if tiene_permiso:
            print("Es menor de edad pero tiene permiso")
        else:
            print("Es menor de edad y no tiene permiso")
    else:
        print("Es mayor de edad")
        if not tiene_permiso:
            print("Pero no tiene permiso")
    mostrar_seccion("Versión simplificada usando and/elif")
    if edad < 18 and tiene_permiso:
        print("Es menor de edad pero tiene permiso")
    elif edad < 18:
        print("Es menor de edad y no tiene permiso")
    elif not tiene_permiso:
        print("Es mayor de edad pero no tiene permiso")
    else:
        print("Es mayor de edad y tiene permiso")
    esperar_enter()

    # EJERCICIO 5
    limpiar_pantalla()
    mostrar_titulo("EJERCICIO 5: ORDEN DE CONDICIONES")
    nota = 85
    if nota >= 90:
        print("Sobresaliente")
    elif nota >= 70:
        print("Notable")
    elif nota >= 60:
        print("Aprobado")
    else:
        print("Suspenso")
    esperar_enter()

    # EJERCICIO 6
    limpiar_pantalla()
    mostrar_titulo("EJERCICIO 6: OPERADOR TERNARIO")
    edad = 20
    estado = "Mayor de edad" if edad >= 18 else "Menor de edad"
    nivel = "Niño" if edad < 13 else "Adolescente" if edad < 18 else "Adulto"
    print(f"estado: {estado}")
    print(f"nivel: {nivel}")
    esperar_enter()

    # EJERCICIO 7
    limpiar_pantalla()
    mostrar_titulo("EJERCICIO 7: IS VS ==")
    a = [1,2,3]
    b = [1,2,3]
    c = a
    print(f"a == b: {a == b}")
    print(f"a is b: {a is b}")
    print(f"a == c: {a == c}")
    print(f"a is c: {a is c}")
    print("\nEjemplo con None:")
    x = None
    print(f"x is None: {x is None}")
    esperar_enter()

    limpiar_pantalla()
    esperar_enter("Presiona Enter para finalizar...")
    limpiar_pantalla()
if __name__ == "__main__":
    main()
