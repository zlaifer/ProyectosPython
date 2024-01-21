from abc import ABC, abstractclassmethod

# Interfaz para caluclar el area
class CalcularArea(ABC):
    @abstractclassmethod
    def calcular_area(self):
        pass