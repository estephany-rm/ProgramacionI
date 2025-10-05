# Ejercicios Prácticos: Expresiones Aritméticas
# Estephany Ruales Mazo


# Ejercicio 1.1: Predice el Resultado
print(5 + 3 * 2) # Mi predicción: 11
# Resultado real: 11
# Explicación: Se resuelve primero la multiplicacion y despues la suma

# Ejercicio 1.2: Paréntesis
print((5 + 3) * 2) # Mi predicción: 16
# Resultado real: 16
# Explicación: Se resuelve primero los parentesis y depues la multiplicacion

# Ejercicio 1.3: División
print(10 / 2) # Mi predicción: 5.0
print(10 // 2) # Mi predicción: 5
print(10 % 2) # Mi predicción: 0
# Resultado real: 5.0, 5, 0
# Explicación: La primera es division normal, la segunda division entera y la tercera modulo

# Ejercicio 1.4: Potencia
print(2 ** 3) # Mi predicción: 8
print(2 ^ 3) # Mi predicción: 1
# Resultado real: 8, 1
# Explicación: La primera es potencia y la segunda es XOR bit a bit

# Ejercicio 1.5: Negación
print(5 - -3) # Mi predicción: 8
print(-5 * -3) # Mi predicción: 15
# Resultado real: 8, 15
# Explicación: Se aplica ley de signos tanto para -(-) = + como para - * - = +

# NIVEL 2: Intermedio (Expresiones Complejas)
# Ejercicio 2.1: Múltiples Operadores
print(2 + 3 * 4 - 5) # Mi predicción: 9
# Resultado real: 9
# Paso a paso: Primero se resuelve la multiplicacion (3*4) = 12
# Luego se resulve (2+12-5) = 9

# Ejercicio 2.2: División y Multiplicación
print(20 / 4 * 2) # Mi predicción: 10.0
print(20 / (4 * 2)) # Mi predicción: 2.5
# Resultado real: 10.0, 2.5
# Explicación: La primera se resuelve de izquierda a derecha, la segunda primero los parentesis

# Ejercicio 2.3: Módulo en Expresión
print(17 % 5 + 2 * 3)  # Mi predicción: 8
# Resultado real: 8
# Explicación: Primero se realiza el modulo y la multiplicacion y luego suman los resultados

#Ejercicio 2.4: Potencias Anidadas
print(2 ** 3 ** 2) # Mi predicción: 512
print((2 ** 3) ** 2) # Mi predicción: 64
# Resultado real: 512, 64
# Explicación: La primera de derecha a izquierda y la segunda primero el parentesis

#Ejercicio 2.5: Expresión Compleja
print(10 + 5 * 2 - 8 / 4 + 3) # Mi predicción: 21.0
# Resultado real: 21.0
# Explicación: Primero se realiza la multiplicacion y division y luego suma y resta de izq a der

#  NIVEL 3: Avanzado (Problemas del Mundo Real)
# Ejercicio 3.1: Cálculo de Impuestos
# Calcula el total con impuesto del 15% sobre una compra de $100.

price = 100
tax_rate = 0.15

# Escribe la expresión correcta:
impuesto = price * tax_rate 
total = impuesto + price
print(total) # Mi predicción: 115.0
# Resultado real: 115.0
# Explicación: Calculo el impuesto y se lo adiciono al precio inicial

# Ejercicio 3.2: Conversión de Temperatura
# Convierte 25°C a Fahrenheit usando la fórmula: F = (C × 9/5) + 32

celsius = 25

# Escribe la expresión:
fahrenheit = (celsius * 9 / 5) + 32
print(fahrenheit) # Mi predicción: 77.0
# Resultado real: 77.0
# Explicación: Se resuelve por formula para convertir de °C a F

# Ejercicio 3.3: Promedio de Calificaciones
# Calcula el promedio de 3 calificaciones: 85, 90, 78

grade1 = 85
grade2 = 90
grade3 = 78

# Escribe la expresión correcta:
average = (grade1+grade2+grade3)/3  # Mi predicción: 84.333...
print(average)
# Resultado real: 84.333...
# Explicación: Formula del promedio se suman los elementos y se divide por la cantidad

# Ejercicio 3.4: Dividir Cuenta
# 4 amigos van a cenar. La cuenta es $127.50. Calcula cuánto paga cada uno.

total_bill = 127.50
num_people = 4

per_person = total_bill/num_people 
print(per_person) # Mi predicción: 31.875
# Resultado real: 31.875
# Explicación: Divido la cuenta en el numero de personas

# Ejercicio 3.5: Tiempo Restante
# Tienes 125 minutos. ¿Cuántas horas y minutos son?

total_minutes = 125

hours = total_minutes//60 # 2 Horas
minutes = total_minutes % 60 # 5 minutos
# Explicación: Utilizo division entera para las horas y modulo para los minutos

# Ejercicios de Debugging
# Debug 1: Encuentra el Error
# Este código debería calcular el promedio
a = 10
b = 20
c = 30
# average = a + b + c / 3 Expresion erronea
average = (a + b + c)  / 3 # Expresion corregida, primero las sumas luego la division
print(f"Promedio: {average}")

# Debug 2: Encuentra el Error
# Calcular 20% de descuento sobre $50
price = 50
discount = 20
# final = price - discount * price Expresion erronea
final = price - (discount * price/100) # Expresion corregida, primero el 20% es 20/100 y entre parentesis
print(f"Precio final: ${final}")