''' 
► Enunciado:
Escribir un programa en el cual Dados 5 números enteros solicitados al usuario, determinar cuál de los 4 números enteros es más cercano al primero.
'''
import random

# Definicion de variables
numero_cercano = 0
# Generación de numeros aleatorios
generar_valor_aleatorio = lambda: random.randint(1, 100)
lista_numerica = [generar_valor_aleatorio() for _ in range(5)]

primer_valor = lista_numerica[0]
print(f"Lista de valores = {lista_numerica}\n")
valor_ingresado = int(input(f"Ingrese cual es número mas cercano a [{primer_valor}]:\n"))

lista_numerica.sort()
print(f"Lista ordenada = {lista_numerica}")

posicion_primer_valor = lista_numerica.index(primer_valor)
print(f"posicion_primer_valor = [{posicion_primer_valor}]")

posicion_anterior = posicion_primer_valor if posicion_primer_valor - 1 < 0 else posicion_primer_valor - 1
print(f"posicion_anterior = [{posicion_anterior}]")

posicion_siguiente = posicion_primer_valor if len(lista_numerica) - 1 < posicion_primer_valor + 1 else posicion_primer_valor + 1
print(f"posicion_siguiente = [{posicion_siguiente}]")

# Función para retornar la posicion con el valor con menor diferencia
def posicion_con_menor_diferencia(posicion_inicial, posicion_anterior, posicion_siguiente):
    diferencia_posicion_anterior = lista_numerica[posicion_inicial] - lista_numerica[posicion_anterior]
    print(f"diferencia_posicion_anterior = [{diferencia_posicion_anterior}]")
    diferencia_posicion_siguiente = lista_numerica[posicion_siguiente] - lista_numerica[posicion_inicial]
    print(f"diferencia_posicion_siguiente = [{diferencia_posicion_siguiente}]")
    if diferencia_posicion_anterior <= diferencia_posicion_siguiente:
        return lista_numerica[posicion_anterior]
    else:
        return lista_numerica[posicion_siguiente]
    
# Logica que permite identificar cual es el numero mas cercano
if posicion_primer_valor == posicion_anterior:
    numero_cercano = lista_numerica[posicion_siguiente]
elif posicion_primer_valor == posicion_siguiente:
    numero_cercano = lista_numerica[posicion_anterior]
else:
    numero_cercano = posicion_con_menor_diferencia(posicion_primer_valor, posicion_anterior, posicion_siguiente)
print(f"numero_cercano = [{numero_cercano}]")

# Logica que permite validar si la respuesta ingresada por el usuario es correcta
if valor_ingresado not in lista_numerica:
    print(f"El valor ingresado [{valor_ingresado}] NO se encuentra en la lista de valores permitidos!")
elif numero_cercano == valor_ingresado:
    print(f"El valor ingresado [{valor_ingresado}] ES efectivamente el más cercano a [{primer_valor}]")
else:
    print(f"El valor ingresado [{valor_ingresado}] NO es el mas cercano a [{primer_valor}]")    