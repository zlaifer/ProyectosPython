from Circulo import Circulo
from Rectangulo import Rectangulo

# Ejemplo de uso
if __name__ == "__main__":
    rectangulo = Rectangulo(5, 10)
    circulo = Circulo(7)
    
    print(f"Area of rectangle: {rectangulo.calcular_area()}")
    print(f"Area of circle: {circulo.calcular_area()}")