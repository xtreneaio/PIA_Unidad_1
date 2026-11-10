import random  # Importamos la librería para poder generar números al azar para el programa de ejemplo

def analizar_listas(lista1, lista2):
    # 1. Convertimos las dos listas normales en conjuntos (sets)
    # Al hacer esto, si había algún número repetido dentro de la misma lista, 
    # Python lo elimina automáticamente.
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    
    # 2. INTERSECCIÓN (elementos comunes en ambos)
    # Es decir: ¿Qué números están en el conjunto1 Y TAMBIÉN en el conjunto2?
    comunes = conjunto1.intersection(conjunto2)
    
    # 3. UNIÓN (todos los elementos sin duplicados)
    # Es decir: Junta todos los números de ambos grupos, pero sin repetir ninguno.
    todos_juntos = conjunto1.union(conjunto2)
    
    # 4. DIFERENCIA SIMÉTRICA (están en uno o en otro, pero no en ambos)
    # Es decir: Los números "exclusivos" de cada grupo, quitando los que comparten.
    exclusivos = conjunto1.symmetric_difference(conjunto2)
    
    # 5. Creamos el diccionario con los resultados
    # Nota: Uso list() para volver a convertirlos en listas normales antes de
    # guardarlos. Así al imprimirlo se verán con corchetes [] y queda más limpio.
    resultados = {
        "interseccion": list(comunes),
        "union": list(todos_juntos),
        "diferencia_simetrica": list(exclusivos)
    }
    
    return resultados

# ==========================================
# PROGRAMA PARA PONER LA FUNCIÓN A PRUEBA
# ==========================================

# NOTA IMPORTANTE: Al utilizar la librería random, tanto la cantidad de elementos
# como los valores de las listas cambiarán cada vez que ejecutemos el programa. 
# Por tanto, los resultados variarán en cada ejecución.

print("Generando lista 1 ...")
lista_A = []
# Generamos una longitud aleatoria entre 5 y 20 elementos
tamano_A = random.randint(5, 20)
for i in range(tamano_A):
    # Añadimos valores aleatorios entre 1 y 15
    lista_A.append(random.randint(1, 15))

print("Generando lista 2 ...")
lista_B = []
# Generamos otra longitud aleatoria distinta entre 5 y 20 elementos
tamano_B = random.randint(5, 20)
for i in range(tamano_B):
    # Añadimos valores aleatorios entre 1 y 15
    lista_B.append(random.randint(1, 15))

print("¡Listas generadas con éxito!\n")

# Ejecutamos la función pasándole nuestras nuevas listas aleatorias
diccionario_final = analizar_listas(lista_A, lista_B)

# Mostramos los resultados paso a paso
print("-" * 60)
print(f"Lista 1 original ({tamano_A} elementos): {lista_A}")
# Al imprimirlo como set(), mostramos visualmente cómo desaparecen los duplicados
print(f"Conjunto 1 (sin duplicados): {set(lista_A)}")
print("-" * 60)
print(f"Lista 2 original ({tamano_B} elementos): {lista_B}")
print(f"Conjunto 2 (sin duplicados): {set(lista_B)}")
print("-" * 60)

print("RESULTADOS MATEMÁTICOS:")
print("Intersección (comunes):", diccionario_final["interseccion"])
print("Unión (todos juntos):", diccionario_final["union"])
print("Diferencia simétrica (exclusivos):", diccionario_final["diferencia_simetrica"])