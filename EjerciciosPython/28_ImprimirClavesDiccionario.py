''' 
► Enunciado:
Dado un diccionario imprimir todas las claves en pantalla.
► Entrada:

capitals = {
    'France': 'Paris',
    'Canada': 'Ottawa',
    'USA': 'Washington'
}

► Salida:
dict_keys(['France', 'Canada', 'USA'])

___

► Ayuda:
El método keys() se usa para obtener todas las claves de un diccionario. Este método devuelve el tipo de dato dict_keys con todas las claves del diccionario.
El tipo de dato devuelto por el método keys() no es una lista, ya que no puede ser modificada y no es posible agregar elementos.

► Sintaxis:
dictionary.keys()
Donde dictionary es el diccionario del cual queremos obtener todas las claves.
'''

capitals = {
    'France': 'Paris',
    'Canada': 'Ottawa',
    'USA': 'Washington'
}

print(capitals.keys())