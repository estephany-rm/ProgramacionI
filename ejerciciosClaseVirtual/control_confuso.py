# Estephany Ruales

def ejercicio_1_modificacion_lista():
    # Problema: eliminar elementos de una lista mientras se itera sobre ella.
    numeros = [1, 2, 3, 4, 5]
    # Resultado del código problemático (explicación):
    # Al remover elementos durante la iteración, el iterador salta elementos
    # porque la lista se reindexa mientras se avanza.
    # Ejemplo (comportamiento observado): queda [1, 3, 5]
    problematic_result = [1, 3, 5]
    print("Ejercicio 1 - resultado problemático esperado:", problematic_result)

    # Solución: nueva lista con los elementos que queremos conservar
    numeros_filtrados = [num for num in numeros if num % 2 != 0]
    print("Ejercicio 1 - solución (números impares):", numeros_filtrados)
    assert numeros_filtrados == [1,3,5]

def ejercicio_2_range():
    # Explicación sobre range()
    # range(10) -> 0..9 ; range(1,10) -> 1..9 ; para 1..10 usar range(1,11)
    print("Ejercicio 2 - ejemplos de range:")
    print("range(10):", list(range(10)))
    print("range(1,10):", list(range(1,10)))
    print("range(1,11):", list(range(1,11)))
    assert list(range(1,11))[-1] == 10

def ejercicio_3_while_correto():
    # El bucle while original olvida incrementar el contador -> bucle infinito.
    contador = 1
    salida = []
    while contador <= 5:
        salida.append(contador)
        contador += 1
    print("Ejercicio 3 - salida esperada:", salida)
    assert salida == [1,2,3,4,5]

def ejercicio_4_break_continue():
    # Mostrar diferencia entre break y continue con ejemplos
    print("Ejercicio 4 - break vs continue:")
    # break: termina el bucle
    salida_break = []
    for i in range(1, 10):
        if i == 5:
            salida_break.append(('break', i))
            break
        salida_break.append(('proc', i))
    print("Con break ->", salida_break)

    # continue: salta la iteración actual
    salida_continue = []
    for i in range(1, 10):
        if i == 5:
            salida_continue.append(('skip', i))
            continue
        salida_continue.append(('proc', i))
    print("Con continue ->", salida_continue)

def ejercicio_5_bucles_anidados_break():
    # Explica que break dentro del bucle interno solo sale de ese bucle.
    matriz = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    objetivo = 6
    encontrado = False
    for fila in matriz:
        for elemento in fila:
            if elemento == objetivo:
                encontrado = True
                break
        if encontrado:
            break
    print("Ejercicio 5 - encontrado:", encontrado)
    assert encontrado == True

def ejercicio_6_comprensiones():
    # Mostrar equivalencia entre bucle tradicional y comprensión de listas
    numeros = list(range(1,11))
    pares_bucle = []
    for num in numeros:
        if num % 2 == 0:
            pares_bucle.append(num**2)
    pares_comp = [num**2 for num in numeros if num % 2 == 0]
    print("Ejercicio 6 - cuadrados de pares (bucle):", pares_bucle)
    print("Ejercicio 6 - cuadrados de pares (comprensión):", pares_comp)
    assert pares_bucle == pares_comp

def main():
    print("== Soluciones para control_confuso.py ==\n")
    ejercicio_1_modificacion_lista()
    print()
    ejercicio_2_range()
    print()
    ejercicio_3_while_correto()
    print()
    ejercicio_4_break_continue()
    print()
    ejercicio_5_bucles_anidados_break()
    print()
    ejercicio_6_comprensiones()
    print("\nTodas las demostraciones han terminado correctamente.")

if __name__ == '__main__':
    main()
