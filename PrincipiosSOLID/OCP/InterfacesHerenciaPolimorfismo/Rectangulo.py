# Clases específicas para cada forma geométrica
from RectanguloCalcularArea import RectanguloCalcularArea
from Forma import Forma

class Rectangulo(Forma):
    def __init__(self, width, height):
        super().__init__(RectanguloCalcularArea(height, width))
        
        