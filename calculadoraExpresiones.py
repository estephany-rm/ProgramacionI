# Estephany Ruales Mazo
# PROYECTO FINAL: Calculadoras de Expresiones

def calculadoraBasica():
    print("*" * 50)
    print("Calculadora básica de expresiones")
    print("*"*50)
    while True:
        expression = input("Ingresa una expresión o 0 para salir: ")
        if expression == "0":
            print("Saliendo del sistema...")
            break
        try:
            resultado = eval(expression)
            print(f"El resultado es: {resultado}")
            print(f"Tipo: {type(resultado).__name__}")
        except ZeroDivisionError:
            print("No se puede dividir por cero.")
        except Exception as e:
            print("Error: Ingresa una expresión válida (solo números y operadores).")

def calculadoraAvanzada():
    print("*" * 50)
    print("Calculadora avanzada de expresiones aritmeticas")
    print("*"*50)
    print("\nOperadores disponibles:")
    print("  +   Suma")
    print("  -   Resta")
    print("  *   Multiplicación")
    print("  /   División")
    print("  //  División entera")
    print("  %   Módulo (resto)")
    print("  **  Potencia")
    historial = []
    while True:
        expression = input("Ingresa una expresión 0 para salir o 1 para mostrar el historial: ")
        if expression == "0":
            print("Saliendo del sistema...")
            break
        elif expression == "1":
            if not historial:
                print("El historial está vacío.")
            else:
                for i in range(len(historial)):
                    print(i+1,". ", historial[i])
            continue
        try:
            resultado = eval(expression)
            historial.append(expression+" = "+str(resultado))
            print(f"El resultado es: {resultado}")
            print(f"Tipo: {type(resultado).__name__}")
        except ZeroDivisionError:
            print("No se puede dividir por cero. Vuelve a intentarlo.")
        except NameError:
            print("Error: variable no definida. Vuelve a intentarlo.")
        except SyntaxError:
            print("Error: Sintaxis inválida. Vuelve a intentarlo.")
        except Exception as e:
            print(f"Error: {e}. Vuelve a intentarlo.")

def main():
    print("-"*50)
    print("ingresando al sistema...")
    print("-"*50)
    resultado = input("Bienvenido a calculadora de expresiones aritmeticas\ndesea utilizar la calculadora basica (1) o la avanzada (2): ")
    if resultado == "1":
        calculadoraBasica()
    elif resultado == "2":
        calculadoraAvanzada()
    else:
        print("Opcion invalida. Saliendo del sistema...")

if __name__ == "__main__":
    main()