''' 
► Enunciado:
Escriba un programa para iterar sobre diccionarios usando bucles for. Se debe mostrar cada clavey valor almacenado.

► Entrada:
dictionary = {'x': 10, 'y': 20, 'z': 30}

► Salida:
x -> 10
y -> 20
z -> 30

► Ayuda:
El método items() devuelve una lista que contiene los pares clave-valor del diccionario, como tuplas en una lista.

dictionary = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
 
dictionary_items = dictionary.items()
print(dictionary_items) 

Se puede utilizar la asignación múltiple en un bucle for para asignar la clave (key) y el valor (value) a variables separadas.

dictionary = {'color1': 'black', 'color2': 'white'}
 
for key, value in dictionary.items():
  print('Key:',key,'|','Value:', value)
'''

diccionario = {'x': 10, 'y': 20, 'z': 30}

for key, value in diccionario.items():
    print(f"{key} -> {value}")
    
 
 
 