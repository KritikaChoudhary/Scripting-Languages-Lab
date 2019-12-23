'''
8a.  (i) Create a dictionary that contains the atomic element symbol and its name. 
(ii)Add a unique & duplicate element into this dictionary by interacting with the user. Observe the output and justify it. 
(iii) Display the number of atomic elements in this dictionary 
(iv) Ask user to enter an element to search in the dictionary. Display appropriate results. 
'''

atom={}

while(1):
    k=input("Atomic symbol:")
    v=input("Atomic name:")
    atom[k]=v
    if(int(input("Continue:1 or Stop:0-"))==0):
        break

print(atom)

print("No. of elements:",len(atom))

'''
searching with value
search=input("Enter element name to search:")
for k in atom:
    if search==atom[k]:
        print("Element:"+k+" Name:"+atom[k])
'''
#searching with key
search=input("Enter element to search:")
for k in atom:
    if search==k:
        print("Element:"+k+" Name:"+atom[k])


