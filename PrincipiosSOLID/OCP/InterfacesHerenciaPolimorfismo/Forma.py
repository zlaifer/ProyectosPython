from abc import ABC
# Clase base para las formas geometricas
class Forma(ABC):
    def __init__(self, calculador_area):
        self.calculador_area = calculador_area
      
    def calcular_area(self):
        return self.calculador_area.calcular_area()