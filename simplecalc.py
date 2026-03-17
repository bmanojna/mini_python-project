# simple calc.for integers
num1 = (int(input("enter a number1: ")))
num2 = (int(input("enter a number2:  ")))
operation = input("enter a operation: ")
if operation == '+':
 print("result",num1+num2)
elif operation == '-':
 print("result",num1-num2)
elif operation == '*':
 print("result",num1*num2)
elif operation == '/':
 print("result",num1/num2)
else :
  print("invalid operation: ")

# simple calculator for float 
num1 = (float(input("enter a num1: ")))
num2 = (float(input("enter a num2: ")))
operation = input("enter a operation: ")
if operation == '+':
   print("result",num1+num2)
elif operation == '-':
   print("result",num1-num2)
elif operation == '*':
   print("result",num1*num2)
elif operation == '/':
   print("result",num1/num2)
else :
   print("invalid opeation: ")

#creating a calculator by using the boolean functions
num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))
operation = input("enter a operation: ")
if operation == '&':
   print("result",num1&num2)
elif operation == '^':
   print("result",num1^num2)
else :
    print("invalid operation")

  
