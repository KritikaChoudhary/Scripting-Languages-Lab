'''
4a. Write a python program to create a class ‘Rectangle’. This class should include a constructor to initialize the dimensions. Include a function in the class to compute the area of the rectangle. Create objects of the class and print area.
'''
class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b

ob1=rectangle(2,3)
print(ob1.area())
