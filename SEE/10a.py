'''
10a. Create a list of 6 numbers. Use ‘list-comprehension’ to create a new list where each element in the original list is multiplied by 3. Use ‘lambda’ and ‘reduce’ function find the sum of the elements of the original list as well as the new list.
'''
from functools import reduce
n=int(input("How many:"))
li=[]
for i in range(0,n):
   li.append(int(input("Enter:")))

print(li)
li2=[i*3 for i in li]
print(li2)

print(reduce(lambda x,y:x+y,li))
print(reduce(lambda x,y:x+y,li2))
