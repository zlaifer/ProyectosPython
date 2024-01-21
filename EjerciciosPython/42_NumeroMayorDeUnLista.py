''' 
► Enunciado:
Escribir un programa que solicite al usuario 3 números, compararlos y decir cual es mayor.
'''
import random

numero_mayor = 0
generar_valor_aleatorio = lambda: random.randint(1, 100)
lista_numerica = [generar_valor_aleatorio() for _ in range(15)]
print(lista_numerica)

def obtener_mayor(numero_1, numero_2):
    if numero_1 > numero_2:
        return numero_1
    return numero_2

for item in lista_numerica:
    if numero_mayor == 0:
        numero_mayor = item
    else:
        numero_mayor = obtener_mayor(item, numero_mayor)
print(f"El numero mayor es [{numero_mayor}]")