import unittest
import mysql.connector
from main import EmployeeDatabase
from unittest.mock import Mock

db = mysql.connector.connect(
            host="localhost",
            user="Daniel",
            password="Goldbergerova1",
            database="EmployeeData")
mycursor = db.cursor()


class TestEmployeeDatabase(unittest.TestCase):
    def setUp(self):
        self.test_emp1 = EmployeeDatabase("John","Doe",30,"M",50000)
        self.test_emp2 = EmployeeDatabase("Steve","Jackson",20,"M",50000)
        self.test_emp3 = EmployeeDatabase("Daniel","Bejček",29,"M",10000)
        # last_row_id recieved as a return from 'add_employee' to monitor the last added and deleted employee
        self.last_row_id,self.added_employee = self.test_emp3.add_employee()

    def tearDown(self):
        self.test_emp1.remove_employee(self.last_row_id)
        print(f"deleted emp_id: {self.last_row_id}")

    def test_database_employee_insert(self):
        """Check to verify that employee has infact been added to the database."""
        get_db_employee = self.test_emp2.get_employee(self.last_row_id)
        # Slice [1:] to exclude the 'emp_id' column and match the result
        self.assertEqual(self.added_employee, get_db_employee[1:], "Incorrect employee")

    def test_add_employee_character_input(self):
        """Check to see if any characters in firstname, lastname and gender are integers or if input is not an empty string."""
        test_firstname = any(char.isdigit() for char in self.test_emp2.firstname) or self.test_emp2.firstname == ""
        test_lastname = any(char.isdigit() for char in self.test_emp2.lastname) or self.test_emp2.lastname == ""
        test_gender = any(char.isdigit() for char in self.test_emp2.gender) or self.test_emp2.gender == ""

        """Check to see if age or salary are not a string."""
        if isinstance(self.test_emp2.age, int) and isinstance(self.test_emp2.salary, int):
            has_string = False
        else:
            has_string = True

        self.assertFalse(has_string, "age or salary cannot be string")
        self.assertFalse(test_firstname, "firstname cannot be an empty string or contain integers")
        self.assertFalse(test_lastname, "lastname cannot be an empty string or contain integers")
        self.assertFalse(test_gender, "gender cannot be an empty string or contain integers")

