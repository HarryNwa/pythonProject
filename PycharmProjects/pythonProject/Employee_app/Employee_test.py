import unittest

import Employee_app
from Employee_app.Employee import Employee


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("Harry Nwa", "Product Development")
        self.employee2 = Employee("James Ikenna", "Product Manager")

    def test_that_employee_app_exists(self):
        self.assertTrue(self.employee)

    def test_that_employee_has_department(self):
        self.assertEqual("Product Development", self.employee.employee_department)


    def test_that_employee_salary_can_be_calculated(self):
        self.employee.calculate_employee_salary(3, 10)
        self.assertEqual(30, self.employee.calculate_employee_salary(3, 10))

    def test_that_employee_had_id(self):
        first_employee = Employee("Udoka Anyanwu", "Visual Quality Assurance")
        second_employee = Employee("Nwoke Ugwumba", "Estate Manager")
        self.assertEqual(3, first_employee.employee_id, second_employee.employee_id)

    def test_that_employee_details_can_print(self):
         employee_details = "Harry Nwa 1 Product Development"
         self.assertEqual(employee_details, self.employee.print_employee_details())
         employee_details = "James Ikenna 2 Product Manager"
         self.assertEqual(employee_details, self.employee2.print_employee_details())




if __name__ == '__main__':
    unittest.main()
