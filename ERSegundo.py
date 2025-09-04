# Estephany Ruales Mazo
# Programación I

from itertools import product
def maximizarResultado():
    # obtengo k y m
    k, m = map(int, input().split())
    listas = []
    maximoResultado = 0
    # construyo las listas
    for i in range(k):
        datos = list(map(int, input().split()))
        listas.append(datos[1:])
    # calculo el resultado maximo    
    for combinacion in product(*listas):
        lista = []
        for iterable in combinacion:
            lista.append(iterable ** 2)
        resultado = sum(lista) % m
        if resultado > maximoResultado:
            maximoResultado = resultado
    return maximoResultado
print(maximizarResultado())
