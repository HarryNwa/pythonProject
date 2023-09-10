from random import random


class Employee:
    employee_id_counter = 0
    employee_name = None
    employee_salary = 0
    employee_department = None
    hourly_rate = 10

    def __init__(self, employee_name: str, employee_department: str):
        Employee.employee_id_counter += 1
        self.employee_id = Employee.employee_id_counter
        self.employee_name = employee_name
        self.employee_department = employee_department

    def get_employee_id(self):
        return self.employee_id

    def employee_assigned_department(self):
        return self.employee_department == "Product Development"

    def calculate_employee_salary(self, number_of_hours_worked, hourly_rate):
        salary = hourly_rate * number_of_hours_worked
        return salary

    def print_employee_details(self):
        employee_details = f"{self.employee_name} {self.employee_id} {self.employee_department}"
        return employee_details
