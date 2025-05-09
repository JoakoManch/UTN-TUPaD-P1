# Ejercicio 1: Imprimir números del 0 al 100
for i in range(101):
    print(i)

# Ejercicio 2: Contar dígitos de un número
numero = int(input("\nIngresa un número entero: "))
cantidad_digitos = len(str(abs(numero)))
print("Cantidad de dígitos:", cantidad_digitos)

# Ejercicio 3: Sumar números entre dos valores (excluyendo extremos)
inicio = int(input("\nIngresa el primer número: "))
fin = int(input("Ingresa el segundo número: "))
if inicio > fin:
    inicio, fin = fin, inicio
suma = 0
for i in range(inicio + 1, fin):
    suma += i
print("La suma es:", suma)

# Ejercicio 4: Sumar números hasta que el usuario ingrese 0
suma = 0
while True:
    numero = int(input("\nIngresa un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero
print("Suma total:", suma)

# Ejercicio 5: Juego de adivinanza
import random
objetivo = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("\nAdivina el número (0-9): "))
    intentos += 1
    if intento == objetivo:
        print(f"¡Correcto! Lo adivinaste en {intentos} intentos.")
        break
    else:
        print("Incorrecto. Intenta de nuevo.")

# Ejercicio 6: Números pares del 100 al 0
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

# Ejercicio 7: Suma de 0 a número ingresado
n = int(input("\nIngresa un número entero positivo: "))
suma = sum(range(n + 1))
print("La suma es:", suma)

# Ejercicio 8: Contar pares, impares, positivos y negativos
total = 100  # Cambiar para pruebas
pares = impares = positivos = negativos = 0
for _ in range(total):
    num = int(input("\nIngresa un número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

# Ejercicio 9: Calcular media de 100 números
suma = 0
total = 100  # Cambiar para pruebas
for _ in range(total):
    num = int(input("\nIngresa un número: "))
    suma += num
media = suma / total
print("La media es:", media)

# Ejercicio 10: Invertir los dígitos de un número
numero = input("\nIngresa un número: ")
invertido = numero[::-1]
print("Número invertido:", invertido)
