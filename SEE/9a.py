'''
9a. Create a Python class called ‘Student’ having ‘name’, ‘age’ as attribute along with a list having the marks obtained for three subjects.  
(i) Create a constructor to initialize two objects of this class. 
(ii) Create a member function called ‘display’ printing the details of a specific object 
(iii) Ask user to enter the values for an object through an ‘accept’ member function. 
(iv) Display these details.
'''
class Student:
    name=""
    age=-1
    def __init__(self):
        self.name="Null"
        self.age=-1
    def accept(self):
        self.name=input("Enter name:")
        self.age=input("Enter age:")
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

Student1=Student()
Student2=Student()
print("**Accept**")
Student1.accept()
Student2.accept()
print("**Display**")
Student1.display()
Student2.display()
