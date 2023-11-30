import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="Daniel",
    password="Goldbergerova1",
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

        if any(value == "" for value in [self.firstname, self.lastname, self.gender]):
            raise TypeError("Value cannot be empty")

        if any(char.isdigit() for char in self.firstname + self.lastname + self.gender):
            raise TypeError("Characters cannot be numbers")

        if (not isinstance(self.age, int) or not isinstance(self.salary, int)) or self.age < 1 or self.salary < 1:
            raise ValueError("Input must be a number and above zero")

        else:
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

# mycursor.execute("ALTER TABLE employees MODIFY COLUMN emp_id INT default = 1")
# mycursor.execute("ALTER TABLE employees AUTO_INCREMENT = 1")
# mycursor.execute("DELETE FROM employees WHERE emp_id BETWEEN 10 AND 20")


emp2.add_employee()
# emp3.remove_employee(109)
# emp2.remove_multiple_employees(114,122)
# emp1.add_multiple_employees(multi_emp)
# emp1.get_employee(27)



