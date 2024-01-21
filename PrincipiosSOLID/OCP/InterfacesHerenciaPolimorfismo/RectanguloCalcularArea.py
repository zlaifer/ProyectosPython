# Implementaciones específicas de AreaCalculator para cada forma
from CalcularAreaInterfaz import CalcularArea

class RectanguloCalcularArea(CalcularArea):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def calcular_area(self):
        return self.width * self.height