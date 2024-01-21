''' 
► Enunciado:
En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

► Entrada:
lista = [20, 50, "Curso", 'Python', 3.14]
'''

lista = [20, 50, "Curso", 'Python', 3.14]
print(lista)
dato_1 = input("Ingrese primer valor:\n")
dato_2 = input("Ingrese segundo valor:\n")

# Por posicion
lista[0] = dato_1
# Por valor, pero toca igual pasarle la posicion y lo obtenemos con index
lista[lista.index(50)] = dato_2
print(lista)

