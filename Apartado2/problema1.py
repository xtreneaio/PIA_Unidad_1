import random
def procesar_lista(numeros):
    # Creamos una lista vacía para ir guardando los números válidos
    lista_limpia = []
    
    # Recorremos la lista original número por número
    for numero in numeros:
        # 1. Comprobamos que el número no sea negativo (que sea 0 o mayor)
        if numero >= 0:
            # 2. Comprobamos que no esté ya en nuestra nueva lista para evitar repetidos
            if numero not in lista_limpia:
                # Si cumple ambas cosas, lo añadimos
                lista_limpia.append(numero)
                
    # 3. Ordenamos la lista resultante de menor a mayor
    lista_limpia.sort()
    
    return lista_limpia


#Función para probar la función de Procesar Listas del Problema 1
def generar_lista_aleatoria(cantidad):
    # Creamos una lista vacía donde iremos metiendo los números
    lista_nueva = []
    
    # El bucle se repetirá el número de veces que le indiquemos en 'cantidad'
    for i in range(cantidad):
        # Generamos un número aleatorio entre -50 y 50 (ambos incluidos)
        numero_al_azar = random.randint(-50, 50)
        
        # Añadimos ese número a nuestra lista
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

mi_lista_prueba = generar_lista_aleatoria(25)
for i in range(1,6):
    lista_prueba = generar_lista_aleatoria( random.randint(15,25) )
    resultado = procesar_lista(lista_prueba)
    print("________________________________________________________")
    print("Ejemplo ", i, ":")
    print("Lista Generada: ", lista_prueba)
    print("Lista procesada: ",resultado)
    print("________________________________________________________")
    

    