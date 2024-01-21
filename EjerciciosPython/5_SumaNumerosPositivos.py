'''Escribir un programa que lea un entero positivo, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1. La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:'''

suma = 0.0
numero = int(input("Ingrese un número entero a sumar:\n"))

suma = numero * (numero + 1)/ 2

print(f"La suma desde el 1 hasta {numero} es {suma}")
