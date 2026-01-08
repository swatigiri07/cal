print(" press 1 for add")
print(" press 2 for sub")
print(" press 3 for multiply")
print(" press 4 for divide")
print(" press 5 for modules")

n = int(input("enter ur choice"))
def add():
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    print(a + b)
def sub():
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    print(a - b) 
def multiply():
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    print(a * b)
def divide():
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    print(a / b)  
def modules():
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    print(a % b)
if n==1:
    add()
elif n==2:
    sub()
elif n==3:
    multiply()
elif n==4:
    divide()
elif n==5:
    modules()
else:
    print("pls select right option: ")        
