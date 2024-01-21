# Clases específicas para cada forma geométrica
from CirculoCalcularArea import CirculoCalcularArea
from Forma import Forma

class Circulo(Forma):
    def __init__(self, radius):
        super().__init__(CirculoCalcularArea(radius))
        
        