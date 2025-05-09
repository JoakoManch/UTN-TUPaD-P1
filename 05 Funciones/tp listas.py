# Ejercicio 1: Lista de múltiplos de 4 del 1 al 100
multiplos_de_4 = list(range(4, 101, 4))
print("Múltiplos de 4:", multiplos_de_4)

# Ejercicio 2: Mostrar el penúltimo elemento de una lista
mi_lista = ["pizza", "chocolate", "helado", "papas", "tacos"]
print("Penúltimo elemento:", mi_lista[-2])

# Ejercicio 3: Lista vacía y uso de append
lista_vacia = []
lista_vacia.append("sol")
lista_vacia.append("luna")
lista_vacia.append("estrella")
print("Lista resultante:", lista_vacia)

# Ejercicio 4: Reemplazo en lista de animales
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print("Animales modificados:", animales)

# Ejercicio 5: Análisis del programa con remove y max
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))  # Elimina el mayor número (22)
print("Lista sin el mayor número:", numeros)

# Ejercicio 6: Lista con saltos de 5 del 10 al 30
lista_saltos = list(range(10, 31, 5))
print("Dos primeros elementos:", lista_saltos[:2])

# Ejercicio 7: Reemplazo de valores centrales en lista
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["coupé", "camioneta"]
print("Lista de autos modificada:", autos)

# Ejercicio 8: Crear lista con dobles
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("Lista de dobles:", dobles)

# Ejercicio 9: Operaciones sobre lista de compras
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print("Lista de compras modificada:", compras)

# Ejercicio 10: Lista anidada con varios tipos
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print("Lista anidada:", lista_anidada)
