# python_no_opt.py
# Versión: 1.0.0
# Versión: 1.0.1 - Blanca
#- Se dismunuyo el codigo al eliminar las ramas innecesarias (else), el if anidado 
#- Se remplazo el bloque if-else por abs
# Versión 1.1.0 - Román
#- Se cambio el tipo del array de frecuencias
#- Se reestructuro el codigo para encontar la moda
#- Se simplifico la estructura para encontar la suma de moda

# El código Python recorre una lista de enteros construyendo una estructura de frecuencias para cada valor,
#determina el valor modal (el que más aparece) y calcula la suma de dígitos de ese valor; utiliza while y for
#junto con if/else anidados para las búsquedas y los conteos. El código en C itera los enteros desde 2 hasta N,
#comprueba la primalidad de cada número probando divisores, acumula el conteo y la suma de los primos encontrados y
#clasifica cuántos son pares y cuántos impares, empleando for, while e if/else anidados en el proceso.


numeros = [3, -1, 0, 5, -7, 0, 2, 3, 3, -1, 5, 5, 5]  # ejemplo; en práctica puede venir de input

# Contadores y estructuras iniciales
frecuencias = {}   #Mod 1.1.0 lista de frecuencias construido como diccionario
i = 0

# Construir lista de valores únicos y sus cuentas de forma O(n^2)
# Mod 1.1.0 Se restructuro para usar diccionario en vez de duplas 
while i < len(numeros):
    val = numeros[i]
    if not val in frecuencias:
        # si no estaba, contar cuántas veces aparece
        cnt = 0
        k = 0
        while k < len(numeros):
            if numeros[k] == val:
                cnt = cnt + 1
                frecuencias.update({val:cnt}) #Mod 1.1.0 se actualizo para usar .update en vez de .append
                #Mod 1.0.1 Se elimino la rama vacía que aumentaba la complejidad visual...
            k = k + 1
    i = i + 1

# Encontrar el valor modal (mayor cuenta). Si hay empate, se elige el primero encontrado.
# mod 1.1.0 se cambio para funcionar con diccionarios
i=0
B=0
while i < len(numeros):
    val = numeros[i]
    A = frecuencias.get(val)
    if A > B:
        B=A
        modo=val
    i=i+1
    
# Sumar dígitos del valor modal (manejo de negativos)
# Mod 1.0.1 Se remplazo el bloque if para utilizar abs...
# Mod 1.1.0 Se reestructuro el bloque entero a una sola linea
suma_digitos=abs(modo*frecuencias.get(val))

# Salidas
print("Frecuencias:", frecuencias)
print("Moda:", modo, "con cuenta:", frecuencias.get(val))
print("Suma de dígitos del modo:", suma_digitos)