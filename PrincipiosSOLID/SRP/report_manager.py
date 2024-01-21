class ReportManager:
    def generate_employee_report(self, employees):
        # Lógica para generar un informe basado en la lista de empleados
        report = "<================== Employee Report ==================>\n"
        for employee in employees:
            report += f"Employee Name: {employee}\n"
        return report