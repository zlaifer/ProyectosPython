''' 
► Enunciado:
Programa que solicite al usuario los datos para calcular el área de un Círculo (●), finalmente mostrar el resultado en pantalla.
► Fórmula: Área del Círculo
Area = PI*(Radio**2)
'''
import math

area = 0.0
radio = float(input("Ingrese el radio del circulo:\n"))
area = math.pi*(radio**2)
print(f"El area del circulo es {area}")
