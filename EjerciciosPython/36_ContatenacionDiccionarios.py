''' 
► Enunciado:
Escriba un script para concatenar dos diccionarios y crear uno nuevo.

► Entrada:
dictionary1 = {'one':1,'two':2}
dictionary2 = {'three':3,'four':4}

► Salida:
{'one': 1, 'two': 2, 'three': 3, 'four': 4}

► Ayuda:
El método update() actualiza un diccionario agregando los pares clave-valor en un segundo diccionario. Este método no devuelve nada.

# Declaración de diccionarios
versiones = {'python':3.9, 'java':17}
version_adicional = {'django':4.2}
 
print("Diccionario original :", versiones)
print("Diccionario a agregar:",version_adicional)
 
# Se Agrega el diccionario con el método update()
versiones.update(version_adicional)
 
print("Nuevo Diccionario:",versiones)
'''

diccionario_1 = {'one':1,'two':2}
diccionario_2 = {'three':3,'four':4}
diccionario_3 = {'five':5,'six':6}
diccionario_4 = {'seven':7,'eight':8}
diccionario_concatenado = {}

for diccionario in [diccionario_1, diccionario_2, diccionario_3, diccionario_4]:
    diccionario_concatenado.update(diccionario)

print(diccionario_concatenado)