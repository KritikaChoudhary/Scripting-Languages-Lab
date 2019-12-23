'''
12a. Create a Python class called ‘Student’ having ‘name’, ‘age’ as attribute along with a list having the marks obtained for three subjects.  
(i) Create a constructor to initialize two objects of this class. 
(ii) Create a member function called ‘display’ printing the details of a specific object 
(iii) Ask user to enter the values for an object through an ‘accept’ member function. 
(iv) Display these details.
'''

class Student:
    def __init__(self,n,a,l):
        self.name=n
        self.age=a
        self.li=l
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Marks")
        for i in self.li:
            print(i)
    def accept(self):
        self.name=input("Enter name:")
        self.age=input("Enter age:")
        print("Enter marks of 3 subjects:")
        for i in range(3):
            self.li.append(input("Mark"+ str(i+1)+":"))

Student1=Student("Nil",-1,[])
Student2=Student("Nil",-1,[])

print("***Enter Details**")
Student1.accept()
Student2.accept()

print("**Details Entered**")
Student1.display()
Student2.display()

            
