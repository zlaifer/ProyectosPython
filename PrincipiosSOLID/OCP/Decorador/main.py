""" 
Ejemplo que utiliza el Principio de Abierto/Cerrado (OCP) en el contexto de clases que representan carros. 
En este ejemplo, implementaré una clase base Car y luego usaré decoradores para agregar nuevas funcionalidades, 
como la capacidad de calcular el consumo de combustible y la velocidad máxima.
"""

from abc import ABC, abstractmethod

# Interfaz para el cálculo del consumo de combustible
class FuelConsumptionCalculator(ABC):
    @abstractmethod
    def calculate_fuel_consumption(self):
        pass

# Clase base para carros
class Car(FuelConsumptionCalculator):
    def __init__(self, model, year):
        self.model = model
        self.year = year

    @abstractmethod
    def display(self):
        pass

    def calculate_fuel_consumption(self):
        return "Fuel consumption not available for this car."

# Decorador base para el cálculo del consumo de combustible
class FuelConsumptionDecorator(FuelConsumptionCalculator):
    def __init__(self, car):
        self._car = car

    @abstractmethod
    def calculate_fuel_consumption(self):
        pass

# Decorador concreto para agregar funcionalidad de calcular consumo de combustible
class FuelConsumptionCalculationDecorator(FuelConsumptionDecorator):
    def calculate_fuel_consumption(self):
        return f"Fuel consumption for {self._car.display()}: 10 liters per 100 km"

# Decorador concreto para agregar funcionalidad de velocidad máxima
class MaxSpeedDecorator(FuelConsumptionDecorator):
    def calculate_fuel_consumption(self):
        return self._car.calculate_fuel_consumption()

    def get_max_speed(self):
        return f"The maximum speed for {self._car.display()} is 200 km/h"

# Implementación concreta de Car: Sedan
class Sedan(Car):
    def display(self):
        return f"Sedan - Model: {self.model}, Year: {self.year}"

# Implementación concreta de Car: SUV
class SUV(Car):
    def display(self):
        return f"SUV - Model: {self.model}, Year: {self.year}"

# Ejemplo de uso
if __name__ == "__main__":
    sedan = Sedan("Toyota Camry", 2022)
    suv = SUV("Jeep Grand Cherokee", 2022)

    # Decorar los carros con funcionalidades adicionales
    sedan_with_fuel_consumption = FuelConsumptionCalculationDecorator(sedan)
    suv_with_max_speed = MaxSpeedDecorator(suv)

    # Mostrar información y funcionalidades adicionales
    print(sedan_with_fuel_consumption.calculate_fuel_consumption())
    print("\n")
    print(suv_with_max_speed.calculate_fuel_consumption())
    print(suv_with_max_speed.get_max_speed())
