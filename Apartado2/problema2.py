def contar_palabras(lista_palabras, ruta_fichero):
    # 1. Leer el contenido del archivo
    with open(ruta_fichero, 'r', encoding='utf-8') as archivo:
        texto = archivo.read()
        
    # 2. Convertir todo el texto a minúsculas
    texto = texto.lower()
    
    # 3. Eliminar los signos de puntuación
    signos_puntuacion = ".,;:!¡¿?()\"'-"
    for signo in signos_puntuacion:
        texto = texto.replace(signo, " ")
        
    # 4. Trocear el texto en palabras sueltas
    palabras_del_texto = texto.split()
    
    # 5. Crear el diccionario y empezar a contar
    diccionario_frecuencias = {}
    
    for palabra_buscada in lista_palabras:
        diccionario_frecuencias[palabra_buscada.lower()] = 0
        
    for palabra in palabras_del_texto:
        if palabra in diccionario_frecuencias:
            diccionario_frecuencias[palabra] += 1
            

# 6. ORDENAR el diccionario por la palabra (la clave) - 
# NOTA: a partir de la versión 3.7 de Python se incorporan mejoras a los diccionarios que permiten ordenarlos de manera sencilla

    diccionario_ordenado = dict(sorted(diccionario_frecuencias.items()))
            
    return diccionario_ordenado

# ==========================================
# PROGRAMA PARA PONER LA FUNCIÓN A PRUEBA
# ==========================================

# A. Creamos el fichero de texto de prueba
ruta_prueba = "mi_texto_prueba.txt"

with open(ruta_prueba, 'w', encoding='utf-8') as f:
    # El principio original
    f.write("¡Hola Mundo! Este es un texto de prueba.\n")
    f.write("El mundo es muy grande, pero este texto es pequeño.\n")
    f.write("Hola de nuevo, mundo.\n")
    f.write("Actualmente estoy inmerso en el Curso de Especialización en Inteligencia Artificial y Big Data.\n")
    f.write("Estamos aprendiendo Python a fondo en la asignatura de PIA.\n")
    f.write("Un saludo para los profesores y compañeros del IES Augustóbriga en Navalmoral de la Mata.\n")
    f.write("Pronto estaremos dominando los modelos de datos y la inteligencia artificial.\n")

# B. Lista de palabras a buscar
palabras_a_buscar = ["hola", "mundo", "texto", "grande", "python", "gato"]

# C. Ejecutamos nuestra función (ahora ya nos lo devuelve ordenado)
resultado = contar_palabras(palabras_a_buscar, ruta_prueba)

# D. Mostrar el resultado (mucho más sencillo ahora)
print("=== RESULTADOS DE FRECUENCIA ===")
for palabra, frecuencia in resultado.items():
    print(f"La palabra '{palabra}' aparece {frecuencia} veces.")


