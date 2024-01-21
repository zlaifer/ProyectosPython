# Implementaciones específicas de AreaCalculator para cada forma
from CalcularAreaInterfaz import CalcularArea

class CirculoCalcularArea(CalcularArea):
    def __init__(self, radius):
        self.radius = radius
        
    def calcular_area(self):
        return 3.14 * self.radius