1. Investigar cómo se usa el operador módulo (modulus) en python, explicarlo con sus palabras y poner un ejemplo. (1 punto)
El operador módulo, se representa por el símbolo de porcentaje (%), se usa para calcular el residuo o resto de una división entera entre dos números. En lugar de devolver el cociente (el resultado de dividir), devuelve lo que sobra después de hacer la división.
Ejemplo:
print (7%3)

1

2. Crear una lista vacía y llenarla con los números pares del 2 al 50 (2,4,6,8,...,48,50) utilizando un for y un condicional para controlar que sólo los pares se agreguen.  (2 puntos)
pares = []
for i in range(2, 51):
    if i % 2 == 0:
        pares.append(i)
print(pares)

[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]


3. Investigar para qué sirve el comando "break" en un for, explicarlo con sus palabras y hacer un ejemplo. (1 punto)
Sirve para interrumpir y salir de un ciclo de manera inmediata, ignorando las iteraciones que aún quedaban pendientes

numeros = [1, 2, 3, 4, 5]
for n in numeros:
    if n == 3:
        print("se encontró el 3, saliendo del ciclo")
        break
    print(f"revisando el número: {n}")

4. Programar el método find de los strings a mano. (2 puntos) Sugerencia: utilizar break cuando encuentren lo que buscan
palabra = 'banana'
# regresar la posición de la primera 'a'

palabra = "banana"
posicion = -1
for i, letra in enumerate(palabra):
    if letra == 'a':
        posicion = i
        break
print(posicion)

1

5. Imprimir todos los números de la siguiente lista utilizando ciclos: (4 puntos)
lista = [ [1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5] ]
# 1
# 1
# 2
# 1
# 2
# 3
# 1
# 2
# 3
# 4
# 1
# 2
# 3
# 4
# 5

lista = [ [1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5] ]
for sublista in lista:
    for numero in sublista:
        print(numero)
