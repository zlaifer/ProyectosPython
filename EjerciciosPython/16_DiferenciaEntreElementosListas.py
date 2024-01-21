''' 
► Enunciado:
Escriba un programa para obtener la diferencia entre las dos listas.

► Entrada:
list1 = [1, 2, 3, 4]
list2 = [1, 2]

► Salida:
[3,4]
'''
list_a = [1, 2, 3, 4]
list_b = [1, 2, 5]
# Diferencia simetrica
print(set(list_a) ^ set(list_b))
# Respuesta: {3, 4, 5}

# Diferencia de elementos que esta en B pero no en A
print(set(list_a) - set(list_b))
# Respuesta: {3, 4}