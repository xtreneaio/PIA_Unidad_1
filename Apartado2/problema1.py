import random

def procesar_lista(numeros):
    # 1. Eliminamos negativos y duplicados usando un conjunto (set) por comprensión
    # Esto evita la búsqueda lineal repetida (coste cuadrático) y es más eficiente
    sin_repetidos = {numero for numero in numeros if numero >= 0}
    
    # 2. Ordenamos los números resultantes de menor a mayor
    # sorted() recibe el conjunto y devuelve directamente una lista ordenada
    return sorted(sin_repetidos)


# Función para probar la función de Procesar Listas del Problema 1
def generar_lista_aleatoria(cantidad):
    lista_nueva = []
    for i in range(cantidad):
        numero_al_azar = random.randint(-50, 50)
        lista_nueva.append(numero_al_azar)
    return lista_nueva
    
    
# --- Comprobación ---
lista_original = [4, -1, 2, 4, 3, -5, 2]
resultado = procesar_lista(lista_original)

print("Lista ejemplo de enunciado:", lista_original)
print("Lista procesada:", resultado)
print("____________________________________________________________")
print("Otras comprobaciones:")
print("____________________________________________________________")

# --- Comprobación con listas aleatorias ---
for i in range(1, 6):
    lista_prueba = generar_lista_aleatoria(random.randint(15, 25))
    resultado = procesar_lista(lista_prueba)
    print("________________________________________________________")
    print("Ejemplo ", i, ":")
    print("Lista Generada: ", lista_prueba)
    print("Lista procesada: ", resultado)
    print("________________________________________________________")
