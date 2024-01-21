''' 
► Enunciado:
Dado un diccionario imprimir todos los valores en pantalla.

► Entrada:
colors = {
    'color1': 'yellow', 
    'color2': 'blue',
    'color3': 'red',
}

► Salida:
dict_values(['yellow', 'blue', 'red'])

► Ayuda:
El método values() se usa para obtener todos los valores de un diccionario. Este método devuelve el tipo de dato dict_values con todas los valores del diccionario.
El tipo de dato devuelto por el método values() no es una lista, ya que no puede ser modificada y no es posible agregar elementos.

► Sintaxis:
dictionary.values()
Donde dictionary es el diccionario del cual queremos obtener todos los valores.
'''

colors = {
    'color1': 'yellow', 
    'color2': 'blue',
    'color3': 'red',
}

print(colors.values())
 