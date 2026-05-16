# MULTILEVEL INHERITANCE TASK
# 🎯 Scenario: Education System
# 👉 Class 1: School
# school_name
# method → show_school()
# 👉 Class 2: Teacher (inherits School)
# teacher_name
# subject
# method → show_teacher()
# 👉 Class 3: Student (inherits Teacher)
# student_name
# grade
# method → show_student()

class School:
    def __init__(self):
        self.school_name="cjits" 
    def show_school(self):
        print(self.school_name) 
class Teacher(School):
    def __init__(self):
        super().__init__()
        self.teacher_name="sanjana"
        self.subject="python"
        
    def show_teacher(self):
        print(self.school_name)
        
class Student(Teacher):

    def __init__(self,name,grd):
        super().__init__()
        self.student_name=name
        self.grade=grd
        
    def show_student(self):
        print(self.school_name)
        print(self.student_name)
        print(self.grade)
        print(self.subject)
        print(self.teacher_name)

s1=Student("sanju","A")
s2=Student("sweety","B")
s1.show_student()
s2.show_student()


# 🧑‍💻 Task:
# Create 2 students
# Use super() in all classes
# Print full hierarchy details
# 👉 Goal:
#  Understand chain inheritance



# HIERARCHICAL INHERITANCE TASK
# 🎯 Scenario: Food Delivery App
# 👉 Parent: User
# name
# location
# method → login()
# 👉 Child 1: Customer
# order_item
# method → place_order()
# 👉 Child 2: DeliveryPartner
# vehicle_type
# method → deliver_order()

class User:
    def __init__(self):
        self.name="hello"
        self.location="hyd"
    def login(self):
        print(self.name)
        print(self.location)
class Customer(User):
    def __init__(self,order_item):
        super().__init__()
        self.order_item=order_item
    def place_order(self):
        print(self.order_item)
class DeliveryPartner(User):
    def __init__(self,vehicle_type):
        super().__init__()
        self.vehicle_type=vehicle_type
    def deliver_order(self):
        print(self.vehicle_type)

s=DeliveryPartner("tata")
c=Customer("horn")

s.login()
s.deliver_order()

c.login()
c.place_order()




        



# 🧑‍💻 Task:
# Create 1 customer and 1 delivery partner
# Use super()
# Show login + role-specific actions
# 👉 Goal:
#  Same base class → different behaviors