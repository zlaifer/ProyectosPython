'''Cree un programa que solicite al usuario su nombre y su edad.   Imprimir un mensaje personalizado con el nombre del usuario que indique el año en el cual la persona cumplirá 100 años.'''

import datetime

ano_actual = datetime.datetime.now().year
nombres = input("Ingrese sus nombre:\n")
edad = int(input("Ingrese su edad:\n"))
anos_faltantes = 100 - edad
ano_en_que_usuario_tiene_100 = ano_actual + anos_faltantes
print(f"Señor/a {nombres} usted cumplirá los 100 en {ano_en_que_usuario_tiene_100}")
