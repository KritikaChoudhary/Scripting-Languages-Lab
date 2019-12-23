'''
1a. Write Python code to do the following:
i.	Create list with inputs from user
ii.	Determine minimum and maximum elements in the list
iii.	Insert new element into the list
iv.	Delete an element from the list
v.	Determine if an element is present in the list.
'''

li=[5,7,2,-9,30,12]
'''
while(1):
    li.append(int(input("Enter:")))
    if(int(input("Conntinue:1 or Stop:0-"))==0):
        break
'''
print(li)
li.sort()     
print(li[0])
print(li[len(li)-1])
li.append(int(input("Enter new element:")))
print(li)
li.remove(li[3])
print(li)
n=int(input("Element to be searched for:"))
for i in li:
    if i==n:
        print(str(i)+"present at"+str(li.index(i)))

