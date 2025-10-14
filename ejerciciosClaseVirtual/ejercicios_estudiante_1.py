# Estephany Ruales Mazo

def ejercicio_1():
    """
    Problema: El siguiente código debería imprimir solo los números impares,
    pero tiene un error porque modifica la lista mientras la recorre.
    Corrígelo para que funcione correctamente.
    """
    numeros = [1,2,3,4,5,6,7,8,9,10]
    # Solución:
    numeros_filtrados = [num for num in numeros if num % 2 != 0]
    print("Ejercicio 1 - lista original:", numeros)
    print("Ejercicio 1 - lista filtrada (solo impares):", numeros_filtrados)
    return numeros_filtrados

def ejercicio_2():
    """
    Problema: Completa el código para generar una tabla de multiplicar
    del 1 al 10 usando bucles anidados.
    """
    print("Ejercicio 2 - Tabla de multiplicar 1 al 10:")
    tabla = {}
    for i in range(1,11):
        fila = []
        for j in range(1,11):
            fila.append(i*j)
        tabla[i] = fila
        # Imprimir la fila formateada
        print(f"{i}: ", end='')
        print(', '.join(str(x) for x in fila))
    return tabla

def ejercicio_3():
    """
    Problema: El siguiente bucle while debería imprimir los números del 1 al 5,
    pero tiene un problema que lo convierte en infinito. Corrígelo.
    """
    print("Ejercicio 3 - imprimir números del 1 al 5:")
    contador = 1
    salida = []
    while contador <= 5:
        salida.append(contador)
        print(f"Número: {contador}")
        contador += 1
    return salida

def ejercicio_4():
    """
    Problema: Usa break y continue adecuadamente para procesar la siguiente lista
    de números: imprime cada número, pero salta los negativos y detén el proceso
    al encontrar un cero.
    """
    numeros = [5, -2, 10, 8, -3, 0, 7, 9]
    print("Ejercicio 4 - procesar lista:", numeros)
    salida = []
    for n in numeros:
        if n < 0:
            # saltar negativos
            continue
        if n == 0:
            # terminar al encontrar cero
            print("Encontrado 0: terminando.")
            break
        print(f"Procesando: {n}")
        salida.append(n)
    print("Resultado final (solo positivos antes de 0):", salida)
    return salida

def ejercicio_5():
    """
    Problema: Reescribe el siguiente código utilizando una comprensión de lista.
    """
    cuadrados_pares = [numero**2 for numero in range(1,11) if numero % 2 == 0]
    print("Ejercicio 5 - cuadrados de pares (comprensión):", cuadrados_pares)
    return cuadrados_pares

def ejercicio_6():
    """
    Problema: Usa bucles anidados para encontrar todas las combinaciones
    posibles de dos listas. Luego implementa el mismo resultado usando
    comprensión de listas.
    """
    colores = ["rojo","azul","verde"]
    tamaños = ["pequeño","mediano","grande"]
    # Con bucles anidados
    combinaciones = []
    for c in colores:
        for t in tamaños:
            combinaciones.append((c,t))
    print("Ejercicio 6 - combinaciones (bucles):", combinaciones)
    # Con comprensión de listas
    combinaciones_comp = [(c,t) for c in colores for t in tamaños]
    print("Ejercicio 6 - combinaciones (comprensión):", combinaciones_comp)
    assert combinaciones == combinaciones_comp
    return combinaciones

def menu():
    """
    Muestra un menú para seleccionar qué ejercicio ejecutar.
    """
    print("\n" + "=" * 50)
    print("EJERCICIOS DE ESTRUCTURAS DE CONTROL".center(50))
    print("=" * 50)
    
    print("\nSelecciona un ejercicio:")
    print("1. Corregir iteración y modificación de lista")
    print("2. Tabla de multiplicar con bucles anidados")
    print("3. Corregir bucle while infinito")
    print("4. Uso de break y continue")
    print("5. Convertir bucle a comprensión de lista")
    print("6. Combinaciones con bucles anidados")
    print("0. Salir")
    
    try:
        opcion = int(input("\nIngresa el número del ejercicio (0-6): "))
        return opcion
    except ValueError:
        print("Entrada inválida. Ingresa un número del 0 al 6.")
        return -1


def main():
    """
    Función principal para ejecutar los ejercicios.
    """
    while True:
        opcion = menu()
        
        if opcion == 0:
            print("¡Hasta luego!")
            break
        elif opcion == 1:
            ejercicio_1()
        elif opcion == 2:
            ejercicio_2()
        elif opcion == 3:
            ejercicio_3()
        elif opcion == 4:
            ejercicio_4()
        elif opcion == 5:
            ejercicio_5()
        elif opcion == 6:
            ejercicio_6()
        else:
            print("Opción inválida. Intenta de nuevo.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()