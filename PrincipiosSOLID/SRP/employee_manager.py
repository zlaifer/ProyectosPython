class EmployeeManager:
    def __init__(self):
        self.employees = []
        
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def delete_employee(self, employee):
        self.employees.remove(employee)
    
    def get_employee_list(self):
        return self.employees