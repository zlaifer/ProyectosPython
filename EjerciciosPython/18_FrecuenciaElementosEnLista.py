''' 
► Enunciado:
Escriba un programa para obtener la frecuencia de los elementos en una lista.

► Entrada:
lista = ['A','A','A','B','B','B','C','C']

► Salida:
Lista Original: ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C']
Frecuencia de Elementos: Counter({'A': 3, 'B': 3, 'C': 2})


► Ayuda:
El módulo collections provee nuevos tipos de datos mejorados que derivan, según el caso, de una lista, una tupla, un diccionario o conjunto de datos (set), nos enfocaremos especificamente en el objeto counter.
Un objeto counter es un contenedor del módulo collections que se utiliza para contar las veces que aparece un valor en una secuencia de caracteres, en una lista, un diccionario o una lista de nombres de argumentos con asignaciones. Este objeto devuelve un diccionario donde:
Las claves son los elementos (sin repetir) de la lista
Los valores el número de veces que aparece cada elemento en la lista.
A continuación, se muestra como construir un objeto counter partiendo de una lista.

import collections
lista = ['Granada', 'Huelva', 'Sevilla', 'Granada', 
         'Granada', 'Sevilla', 'Sevilla']
 
# Se crea un objeto counter a partir de una lista
frecuencia = collections.Counter(lista)
print(frecuencia)
'''
import collections

# Si solo se necesita contar cuantas veces se repite un elemento especifico en una llista, se puede utilizar count() que viene diponible en la clase lista
lista = ['A','A','A','B','B','B','C','C']
elemento_a_buscar = 'B'
print("<================================================================>")
print(f"El elemento => [{elemento_a_buscar}] se repite [{lista.count(elemento_a_buscar)}] veces")
print("<================================================================>")

# Si necesita contar cuantas veces se repiten todos los elementos de una lista, se puede utilizar collections.Counter
lista = ['A','A','A','B','B','B','C','C']
frecuencia = collections.Counter(lista)
print(f"Lista original => {lista}")
print(f"Frecuencia de Elementos => [{frecuencia}]")
print("<================================================================>")