import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="",
    password="",
    database="EmployeeData")
mycursor = db.cursor()

class EmployeeDatabase():
    def __init__(self, firstname, lastname, age, gender, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.salary = salary

    def add_employee(self):
        add_emp = "INSERT INTO employees (first_name, last_name, age, gender, salary) VALUES (%s,%s,%s,%s,%s)"
        values = (self.firstname, self.lastname, self.age, self.gender, self.salary)
        mycursor.execute(add_emp, values)
        db.commit()
        last_row_id = mycursor.lastrowid
        return last_row_id, values

    def add_multiple_employees(self, employees):
        insert_emp = "INSERT INTO employees (first_name, last_name, age, gender, salary) VALUES (%s,%s,%s,%s,%s)"
        mycursor.executemany(insert_emp, employees)
        db.commit()
        return employees

    def remove_employee(self, emp_id):
        delete_emp = f"DELETE FROM employees WHERE emp_id = {emp_id}"
        mycursor.execute(delete_emp)
        db.commit()

    def remove_multiple_employees(self,start_idx,end_idx):
        delete_multiple_emp = f"DELETE FROM employees WHERE emp_id BETWEEN {start_idx} AND {end_idx}"
        mycursor.execute(delete_multiple_emp)
        db.commit()

    def get_employee(self,emp_id):
        get_emp = f"SELECT * FROM employees WHERE emp_id = {emp_id}"
        mycursor.execute(get_emp)
        result = mycursor.fetchone()
        return result


emp1 = EmployeeDatabase("Daniel","Bejček",29,"M",10000)
emp2 = EmployeeDatabase("Tereza","Vojtěchová",25,"F",9000)
emp3 = EmployeeDatabase("John","Doe",30,"M",50000)
multi_emp = [("Daniel","Bejček",29,"M",10000), ("Tereza","Vojtěchová",25,"F",9000)]



