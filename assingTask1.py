# Maths Operations
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

add=num1+num2

if num1>num2:
    sub=num1-num2
else:
    sub=num2-num1

mul=num1*num2

if num2!=0: 
  div=num1/num2
else:
    div="Not defined (division by zero)"

print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)