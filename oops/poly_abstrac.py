'''Create a class Product
Create private variable for price
Add method set_price(price)
Accept only values greater than 0 
Add method apply_discount(percent)
Discount should not exceed 50% 
Update price after discount
Add method get_price()
Return current price
'''

class Product():
    def __init__(self):
        self.__price = 0 
    def set_price(self,price):
        if price > 0:
            self.__price = price
        else:
            print("Price must be greater than 0")

    def apply_discount(self,percent):
        if percent <= 50:
            discount = (self.__price * percent) / 100
            self.__price -= discount
        else:
            print("Discount cannot exceed 50%")

    def get_price(self):
        return self.__price
    
p = Product()
p.set_price(1000)
p.apply_discount(20)
print("Current Price:", p.get_price())
        


''' Instructions:
Create a class Mobile
Create private variable for password
Add method set_password(pwd)
Password must be at least 4 characters
Add method unlock(pwd)
Check password and print result
Add method change_password(old_pwd, new_pwd)
Change only if old password is correct
New password must follow rules
'''

class Mobile():
    def __init__(self):
        self.__password=""
        
    def set_password(self,pwd):
        
        if len(pwd)>=4:
            self.__password=pwd
            print("valid password")
        else:
            print("invalid password (length)")
        
    def unlock(self,pwd):
        if self.__password==pwd:
            print("unlock successful")
        else:
            print("unlock unsuccessful")
        
    def change_password(self,old_pwd, new_pwd):
        if old_pwd==self.__password:
            if len(new_pwd)>=4:
                self.__password=new_pwd
                print("password changed successfully")
            else:
                print("Password must be at least 4 characters")
        else:
            print("old pwd is incorrect")

m=Mobile()
m.set_password("1243")
m.unlock("1243")
m.change_password("1243","acbd")


'''Instructions:
Create a class Employee
Create private variables:
__salary
__designation
Add method set_salary(salary)
Salary should be greater than 0
Prevent invalid updates
Add method get_salary()
Return salary
Add method set_designation(role)
Allow only specific roles (e.g., "Manager", "Developer", "HR")
Add method get_designation()
Return designation
Add method increment_salary(percent)
Increase salary based on percentage
Percentage should not exceed 30%
Do not allow direct access to salary or designation from outside the class'''

class Employee:
    def __init__(self):
        self.__salary=40000
        self.__designation="associate"
    def set_salary(self,salary):
        if salary>0:
            self.__salary=salary
            print("valid salary")
        else:
            print("invalid salary")
    def get_salary(self):
        return self.__salary
    def set_designation(self,role):
        allowed_roles=["manager","developer","hr"]
        if role in allowed_roles:
            self.__designation=role
            print("designation updated successfully")
        else:
            print("invalid designation")
    def get_designation(self):
        return self.__designation
    def increment_salary(self,percent):
        if percent<=30:
            increment=(self.__salary*percent)/100
            self.__salary+=increment
            print("salary incremented successfully")
        else:
            print("increment percentage cannot exceed 30%")

e=Employee()
e.set_salary(50000)
e.set_designation("developer")

print("Salary:", e.get_salary())
print("Designation:", e.get_designation())

e.increment_salary(20)
print("Updated Salary:", e.get_salary())

# Direct access not allowed
# print(e.__salary)  # -> Error
# print(e.__designation) -> Error