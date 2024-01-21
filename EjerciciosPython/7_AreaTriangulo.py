''' 
► Enunciado:
Programa que solicite al usuario los datos para calcular el área de un Triángulo (▲), finalmente mostrar el resultado en pantalla.
► Fórmula: Área del Triángulo
Area = (Base*Altura)/2
'''

area = 0.0
base = float(input("Ingrese la base del triangulo:\n"))
altura = float(input("Ingrese la altura del triangulo:\n"))
area = (base * altura) / 2
print(f"El area del triangulo es {area}")
