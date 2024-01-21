''' 
► Enunciado:
Escriba un programa para eliminar elementos duplicados de una lista.

► Entrada:
numList = [10,20,30,20,10,50,60,40,80,50,40]

► Salida:
[10, 20, 30, 50, 60, 40, 80]

► Ayuda:
En Python existen operadores de pertenencia, se emplean para identificar pertenencia en alguna secuencia (listas, strings, tuplas).
in y not in son operadores de pertenencia.
in devuelve True si el valor especificado se encuentra en la secuencia. En caso contrario devuelve False.
not in devuelve True si el valor especificado no se encuentra en la secuencia. En caso contrario devuelve False.
items_numericos = [1,2,3,4,5]
cadena = "Hello World"
 
print(">>> Está el número 3 en la lista items_numericos?: ") 
print(3 in items_numericos) # Muestra True 
  
print(">>> El número 12 No está en la lista items_numericos?: ")
print(12 not in items_numericos) # Muestra True
 
print(">>> La cadena contiene 'World'?: ")
print("World" in cadena) # Muestra True
 
print(">>> La palabra 'code' no está en la cadena?: ")
print("code" not in cadena) # Muestra True
'''
from asyncio import sleep
import datetime
import random
import time

# Constantes
numero_minimo = 1
numero_maximo = 1000
numero_datos = 1000000
lista_aleatoria = []
# Generación de datos aleatorios
fecha_inicio_datos = datetime.datetime.now()
print(f"Fecha/hora de inicio de generación de datos => [{fecha_inicio_datos}]")
# Inicio de logica
# Sintaxis de una función lambda para generar un valor aleatorio entre 1 y 100
generar_valor_aleatorio = lambda: random.randint(numero_minimo, numero_maximo)
# Utilizar la función lambda para crear una lista de 10 valores aleatorios
lista_aleatoria = [generar_valor_aleatorio() for _ in range(numero_datos)]
# Imprimir la lista resultante
print(f"Número de datos generados [{numero_datos}]")
# Fin de logica
fecha_fin_datos = datetime.datetime.now()
diferencia_datos = fecha_fin_datos - fecha_inicio_datos
print(f"Fecha/hora de finalización de generación de datos => [{fecha_fin_datos}]")
print(f"La generación de datos demoró => [{diferencia_datos.total_seconds()}]")
print("<================================================================>")

time.sleep(5)

# Primera forma de resolverlo
fecha_inicio_f1 = datetime.datetime.now()
print(f"Fecha/hora de inicio de solución 1 => [{fecha_inicio_f1}]")
# Inicio de logica
lista_items_f1 = lista_aleatoria
list_items_unicos_f1 = list(set(lista_items_f1))
list_items_unicos_f1.sort()
print(list_items_unicos_f1)
# Fin de logica
fecha_fin_f1 = datetime.datetime.now()
diferencia_f1 = fecha_fin_f1 - fecha_inicio_f1
print(f"Fecha/hora de finalización de solución 1 => [{fecha_fin_f1}]")
print(f"El proceso demoró => [{diferencia_f1.total_seconds()}]")
print("<================================================================>")

time.sleep(5)

# Segunda forma de resolverlo
list_items_unicos_f2 = []
list_items_duplicados_f2 = set()
fecha_inicio_f2 = datetime.datetime.now()
print(f"Fecha/hora de inicio de solución 2 => [{fecha_inicio_f2}]")
lista_items_f2 = lista_aleatoria
# Inicio de logica
for item in lista_items_f2:
    if item not in list_items_duplicados_f2:
        list_items_unicos_f2.append(item)
        list_items_duplicados_f2.add(item)
list_items_unicos_f2.sort()
print(list_items_unicos_f2)
# Fin de logica
fecha_fin_f2 = datetime.datetime.now()
diferencia_f2 = fecha_fin_f2 - fecha_inicio_f2
print(f"Fecha/hora de finalización de solución 2 => [{fecha_fin_f2}]")
print(f"El proceso demoró => [{diferencia_f2.total_seconds()}]")

print("<================================================================>")
diferencia_soluciones = None
if diferencia_f1 < diferencia_f2:
    diferencia_soluciones = ('Solución 1', (diferencia_f1 - diferencia_f2).total_seconds())
else:
    diferencia_soluciones = ('Solución 2', (diferencia_f2 - diferencia_f1).total_seconds())
    
print("Resumen")
print(f"La [{diferencia_soluciones[0]}] es más eficiente que la otra solución por [{diferencia_soluciones[1]}] segundos")
print("<================================================================>")

# Como conclusión se tiene que la solución 1 es mucho mas eficiente en cuanto a tiempos de procesamiento