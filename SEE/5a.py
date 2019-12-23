'''
5a. Write a temperature converter python program, which is menu driven. Each such conversion logic should be defined in separate functions. The program should call the respective function based on the user’s requirement. The program should run as long as the user wishes so. Provide an option to view the conversions stored as list of tuples with attributes - from unit value, to unit value sorted by the user’s choice (from-value or to-value).
'''
def FtoC(temp):
    c= (temp-32)*5/9
    history.append(str(temp)+"F->"+str(c)+"C")
    return c


def CtoF(temp):
    c=temp*9/5+32
    history.append(str(temp)+"C->"+str(c)+"F")
    return c

def FtoK(temp):
    c=(temp-32)*5/(9*273.15)
    history.append(str(temp)+"F->"+str(c)+"K")
    return c

def KtoF(temp):
    c=temp*(273.15*9)/5+32
    history.append(str(temp)+"K->"+str(c)+"F")
    return c

def CtoK(temp):
    c=temp+273.15
    history.append(str(temp)+"C->"+str(c)+"K")
    return c

def KtoC(temp):
    c=temp-273.15
    history.append(str(temp)+"K->"+str(c)+"C")
    return c

history=[]
while(1):
    print("1.F to C\n2.C to F\n3.F to K\n4.K to F\n5.C to K\n6.K to C\n7.History\n-1.Exit")
    ch=input( "Enter choice:")
    temp=int(input("Enter temperature:"))
    if(ch=="1"):
        print(FtoC(temp))
    elif ch=="2":
        print(CtoF(temp))
    elif ch=="3":
        print(FtoK(temp))
    elif ch=="4":
        print(KtoF(temp))
    elif ch=="5":
        print(CtoK(temp))
    elif ch=="6":
        print(KtoC(temp))
    elif ch=="7":
        print(history)
    elif ch=="-1":
        break
    else:
        print("Wrong Choice")


