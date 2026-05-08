'''Task : 
🧩 Task 1: Student System
👉 Question:
Create a class Student with:
Class variable: school_name = "XYZ School"
A method set_details()
 → inside method, assign:
name = "Vamsi"
marks = 85
A method display()
 → print:
Name
Marks
School name
👉 Outside the class:
Create object
Call set_details()
Call display()'''

class Student:
    school_name = "XYZ School"
    def set_details(self):
        self.name = "Vamsi"
        self.marks = 85
    def display(self):
        print('name',self.name)
        print('marks',self.marks)
        print('School name',Student.school_name)
a=Student()
a.set_details()
a.display()


'''🧩 Task 2: Employee System
👉 Question:
Create a class Employee with:
Class variable: company = "Infosys"
A method set_data()
 → assign:
name = "Ravi"
salary = 20000
A method increase_salary()
 → add 5000 to salary
A method display()
 → print all details
👉 Outside the class:
Create object
Call all methods'''

class Employee: 
    company = "Infosys"
    def set_data(self):
        self.name = "Ravi"
        self.salary = 20000
    def increase_salary(self):
        print(self.name,"name")
        print(self.salary,"salary")
        print(Employee.company,"company")
a=Employee()
a.set_data()
a.increase_salary()


'''🧩 Task 3: Mobile System
👉 Question:
Create a class Mobile with:
Class variable: brand = "Apple"
A method set_details()
 → assign:
model = "iPhone 14"
price = 80000
A method discount()
 → reduce price by 10%
A method show_details()
 → print all details
👉 Outside the class:
Create object
Call methods'''


class Mobile: 
    brand = "Apple"
    def set_details(self):
        self.model = "iPhone 14"
        self.price = 80000
    def discount(self):
        self.price = self.price - (self.price * 10 / 100)
    def show_details(self):    
        print(self.model,"model")
        print(self.price,"price")
        print(Mobile.brand,"barnd")
a=Mobile()
a.set_details()
a.discount()
a.show_details()