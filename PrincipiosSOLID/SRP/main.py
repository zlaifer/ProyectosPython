"""
Supongamos que tenemos una clase que maneja la gestión de empleados y, además, también se encarga de generar informes. 
Esto violaría el SRP, ya que tiene más de una responsabilidad. 
Vamos a dividirlo en dos clases, una para la gestión de empleados y otra para la generación de informes:

Clase EmployeeManager -> Encargada de la getsión de empleados
Clase ReportManager -> Encarga de la gestión de reportes
Clase Application -> Se encarga de ejecutar la logica de negocio
"""

from report_manager import ReportManager
from employee_manager import EmployeeManager

class Application:
    def run(self):
        employee_manager = EmployeeManager()
        report_manager = ReportManager()

        employee_manager.add_employee("Carlos Hernesto")
        employee_manager.add_employee("Jhono Guzman")

        employees = employee_manager.get_employee_list()
        report = report_manager.generate_employee_report(employees)

        print(report)


# Ejecución de la clase
if __name__ == "__main__":
    app = Application()
    app.run()