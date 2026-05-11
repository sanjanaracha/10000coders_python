'''Task : 

🧬 1️⃣ SINGLE INHERITANCE TASK
🎯 Scenario: Online Course Platform
👉 Parent Class: Course
course_name
price
method → show_course()
👉 Child Class: ProgrammingCourse
language
duration
method → show_programming_course()'''

'''🧑‍💻 Task:
Create 2 programming courses
Use super()
Print all details
👉 Expected Thinking:
 “Base course details reused + extra programming details added”'''


class Course():
    def __init__(self, course_name, price):
        self.course_name = course_name
        self.price = price

    def show_course(self):
        print("Course Name:", self.course_name)
        print("Price:", self.price)

class ProgrammingCourse(Course):
    def __init__(self, course_name, price, language, duration):
        super().__init__(course_name, price)   # calling parent constructor
        self.language = language
        self.duration = duration

    def show_programming_course(self):
        self.show_course()
        print("Language:", self.language)
        print("Duration:", self.duration)
        print(self.language)
o1 = ProgrammingCourse("Python Full Stack", 40000, "English", "6 Months")
o2 = ProgrammingCourse("Java Development", 35000, "English", "5 Months")

print("Course 1 Details:")
o1.show_programming_course()

print("\nCourse 2 Details:")
o2.show_programming_course()



'''🧬 2️⃣ MULTIPLE INHERITANCE TASK
🎯 Scenario: Smart Phone Features
👉 Parent 1: Camera
camera_mp
method → take_photo()
👉 Parent 2: MusicPlayer
brand
method → play_music()
👉 Child: SmartPhone
model_name
method → show_details()'''

'''🧑‍💻 Task:
Create 2 smartphones
Call both parent methods
Print all features
👉 Goal:
 Understand using multiple parents in one class'''



class Camera():
    def __init__(self, camera_mp):
        self.camera_mp = camera_mp

    def take_photo(self):
        print("Camera:", self.camera_mp)

class MusicPlayer:
    def __init__(self, brand):
        self.brand = brand

    def play_music(self):
        print("Music Brand:", self.brand)


class SmartPhone(Camera, MusicPlayer):
    def __init__(self, camera_mp, brand, model_name):
        Camera.__init__(self, camera_mp)
        MusicPlayer.__init__(self, brand)
        self.model_name = model_name

    def show_details(self):
        print("Model Name:", self.model_name)
        self.take_photo()
        self.play_music()

# Creating 2 smartphones
s1 = SmartPhone("120 MP", "OPPO", "A17")
s2 = SmartPhone("108 MP", "Samsung", "Galaxy M14")

print("Smartphone 1:")
s1.show_details()

print("\nSmartphone 2:")
s2.show_details()

