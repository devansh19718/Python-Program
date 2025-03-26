def add(x,y):
    print("addition-", x+y)

def subtract(x,y):
    print("subtraction-", x-y)

print("Enter 'add' for addition and subtract for subtraction")
user_input=input()

if user_input== "add":
    num1=int(input())
    num2=int(input())
    add(num1,num2)

elif user_input== "subtract":
    num1-int(input())
    num2-int(input())
    subtract (num1, num2)
else:
    print("Invalid Input")
