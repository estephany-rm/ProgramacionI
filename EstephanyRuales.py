# Jugador A, Jugador B
# Strings y substrings unos por consonantes y otro por vocales
# repeticiones substrings
# ganador A o B cantidad de subcadenas
import pprint as pp
def partidaStrings(string:str):
    vocales = ['a', 'e', 'i', 'o', 'u']
    contadorA = 0 
    jugadorA = []
    jugadorB = []
    contadorB = 0
    
    while True:
        # jugador A
        if string[0] in vocales:
            valoresA = encontrarSub(string, vocales, True)
            jugadorA = valoresA[0]
            contadorA = valoresA[1]
        # jugador B
        if string[0] not in vocales:
            valoresB = encontrarSub(string, vocales, False)
            jugadorB = valoresB[0]
            contadorB = valoresB[1]
        # jugador B si no empieza por consonante
        elif string[1] not in vocales:
            copiaString = string[1:]
            valoresB = encontrarSub(copiaString, vocales, False)
            jugadorB = valoresB[0]
            contadorB = valoresB[1]
        break

    if contadorA > contadorB:
        return "Ganador jugadorA", jugadorA, contadorA
    else:
        return "Ganador jugadorB", jugadorB, contadorB


def encontrarSub(string: str, vocales, esA):
    lista = []
    contador = 0
    for i in range(len(string)):
        if (esA and string[i] in vocales) or (not esA and string[i] not in vocales):
            for j in range(i+1, len(string)+1):
                sub = string[i:j]
                lista.append(sub)
                contador += 1
    return lista, contador


palabra = "murcielago"
pp.pprint(partidaStrings(palabra))