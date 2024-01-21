''' 
► Enunciado:
Escriba un script para imprimir la suma de los valores de un diccionario.

► Entrada:
dictionary = {'data1':10,'data2':-100,'data3':1000}

► Salida:
910

► Ayuda:
La función sum() nos regresa la suma los elementos del iterable de entrada. La estructura de esta función es la siguiente:
sum(iterable, inicio)
iterable es el elemento iterable (lista, tupla, diccionario) con los de valores que se quieren sumar.
inicio es un valor opcional que se debe sumar a los elementos del iterable.

Ejemplos del uso de la función:

# Lista con los elementos a sumar
numeros = [12, 67, 2, 67, 85, 65]
 
print("1 Parámetro : ", sum(numeros))
print("2 Parámetros:" , sum(numeros,1000))
'''

diccionario = {'data1':10,'data2':-100,'data3':1000}
print(sum(diccionario.values()))
