# python_no_opt.py
# Versión: 1.0.0
# Versión: 1.0.1- Se dismunuyo el codigo al eliminar las ramas innecesarias (else), el if anidado y se remplazo el bloque if-else por abs - Blanca

# El código Python recorre una lista de enteros construyendo una estructura de frecuencias para cada valor,
#determina el valor modal (el que más aparece) y calcula la suma de dígitos de ese valor; utiliza while y for
#junto con if/else anidados para las búsquedas y los conteos. El código en C itera los enteros desde 2 hasta N,
#comprueba la primalidad de cada número probando divisores, acumula el conteo y la suma de los primos encontrados y
#clasifica cuántos son pares y cuántos impares, empleando for, while e if/else anidados en el proceso.


numeros = [3, -1, 0, 5, -7, 0, 2, 3, 3, -1, 5, 5, 5]  # ejemplo; en práctica puede venir de input

# Contadores y estructuras iniciales
frecuencias = []   # lista de tuplas (valor, cuenta) construida de forma ineficiente
i = 0

# Construir lista de valores únicos y sus cuentas de forma O(n^2)
while i < len(numeros):
    val = numeros[i]
    # comprobar si ya está en frecuencias (búsqueda lineal)
    encontrado = False
    j = 0
    while j < len(frecuencias):
        if frecuencias[j][0] == val:
            encontrado = True
            # reconstruimos la tupla incrementando manualmente
            viejo_val, viejo_cnt = frecuencias[j]
            nuevo_cnt = viejo_cnt + 1
            frecuencias[j] = (viejo_val, nuevo_cnt)
            # Se elimino la rama que nunca se ejecuta...
        j = j + 1
    if not encontrado:
        # si no estaba, contar cuántas veces aparece
        cnt = 0
        k = 0
        while k < len(numeros):
            if numeros[k] == val:
                cnt = cnt + 1
                # Se elimino la rama vacía que aumentaba la complejidad visual...
            k = k + 1
        frecuencias.append((val, cnt))
    i = i + 1

# Encontrar el valor modal (mayor cuenta). Si hay empate, se elige el primero encontrado.
modo = None
max_cuenta = -1
for pair in frecuencias:
    v = pair[0]
    c = pair[1]
    if c > max_cuenta:
        max_cuenta = c
        modo = v
        # se elimino la rama extra para if anidado...

# Sumar dígitos del valor modal (manejo de negativos)
# Se remplazo el bloque if para utilizar abs...
x = abs(modo)

# sumar dígitos con while
suma_digitos = 0
while x > 0:
    suma_digitos = suma_digitos + (x % 10)
    x = x // 10

# Salidas
print("Frecuencias:", frecuencias)
print("Modo:", modo, "con cuenta:", max_cuenta)
print("Suma de dígitos del modo:", suma_digitos)