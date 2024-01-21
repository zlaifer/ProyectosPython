''' 
► Enunciado:
Escriba un programa para generar todas las permutaciones de una lista.

► Entrada:
numList = [1,2,3]

► Salida:
[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2),
 (3, 2, 1)]
► Ayuda:
El módulo itertools proporcionado por Python, sirve para crear iteradores para un bucle eficiente. Para generar una permutación de elementos, nos enfocaremos en los iteradores combinatorios con itertools.permutations(). La sintaxis es la siguiente:
permutations(iterador, longitud)
La función permutations() toma dos argumentos:
iterador: Elementos a permutar.
longitud (opcional): Extensión o longitud de la permutación. Se asume la longitud predeterminada del iterador, si no se coloca este argumento, devuelve todas las posibles permutaciones según la cantidad de elementos.

from itertools import permutations   
      
print(">>> Permutaciones para una lista:")    
print(list(permutations([1, 'geeks'], 2)))   
   
print(">>> Permutaciones para una cadena:")    
print(list(permutations('AB')))   
      
print (">>>  para un rango de numeros:")    
print(list(permutations(range(3), 2)))
'''
from itertools import permutations

lista_numerica = [1,2,3]
permutaciones = list(permutations(lista_numerica))
print(permutaciones)

