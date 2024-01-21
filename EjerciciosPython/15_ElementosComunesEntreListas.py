''' 
► Enunciado:
Escriba un programa para encontrar elementos comunes de dos listas.

► Entrada:
color1 = "Red", "Green", "Orange", "White"
color2 = "Black", "Green", "White", "Pink"

► Salida:
{'Green', 'White'}

► Ayuda:
El método set() se utiliza para convertir cualquiera de los iterables en una secuencia de elementos iterables con elementos distintos, comúnmente llamado set.
El tipo set en Python es la clase utilizada por el lenguaje para representar los conjuntos. Un conjunto es una colección desordenada de elementos únicos, es decir, que no se repiten.
La clase set también implementa las típicas operaciones matemáticas sobre conjuntos: unión (|), intersección (&), diferencia (-) y unión simétrica (^).
Para crear un conjunto, basta con encerrar una serie de elementos entre llaves {}, o bien usar el constructor de la clase set() y pasarle como argumento un objeto iterable (como una lista, una tupla o una cadena).

# Crea un conjunto con una serie de elementos entre llaves
# Los elementos repetidos se eliminan
conjunto = {1, 3, 2, 9, 3, 1}
print(conjunto)
 
# Crea un conjunto a partir de una lista
# Los elementos repetidos de la lista se eliminan
lista = set([3, 5, 6, 1, 5])
print(lista)
 
# Crea un conjunto a partir de un string o cadena
# Los caracteres repetidos se eliminan
cadena = set('Hola Pythonista')
print(cadena)


Para hallar la unión (|), intersección (&), diferencia (-) o la unión simétrica (^) de dos conjuntos en Python se procede de la siguiente manera:

conjunto_A = {1,2,3,4}
conjunto_B = {5,2,3,6}
 
print(">>> Unión de dos conjuntos:")
# Conjunto de elementos que están en uno , en otro o en ambos.
print(set(conjunto_A) | set(conjunto_B))
 
################################################################
 
print(">>> Intersección de dos Conjuntos:")
# Conjunto de elementos que estan en ambos conjuntos
print(set(conjunto_A) & set(conjunto_B))
 
################################################################
 
print(">>> Diferencia de dos conjuntos:")
# Conjunto de elementos que están en A pero no en B
print(set(conjunto_A) - set(conjunto_B))
 
# Conjunto de elementos que están en B pero no en A
print(set(conjunto_B) - set(conjunto_A))
 
################################################################
 
print(">>> Diferencia simétrica de dos conjuntos:")
# Conjunto de elementos que están en A o B, pero no en ambos
print(set(conjunto_A) ^ set(conjunto_B))
'''
lista_colores_1 = "Red", "Green", "Orange", "White"
lista_colores_2 = "Black", "Green", "White", "Pink"
# Forma resumida:
print(f"Los elementos comunes entre las listas - Forma resumida: [{set(lista_colores_1) & set(lista_colores_2)}]")

set_lista_colores_1 = set(lista_colores_1)
set_lista_colores_2 = set(lista_colores_2)
elementos_comunes = set_lista_colores_1 & set_lista_colores_2
print(f"Los elementos comunes entre las listas: [{elementos_comunes}]")
