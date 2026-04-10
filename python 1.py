#write a program for simple data input using input() and a formatted output using print().
name=input("enter your name: ")
print("hello!!",name )

#implement programs for computing area,simple intrest, and basic arithe3matic expressions.

radius = float(input("Enter radius: "))
area = 3.14 * radius * radius
print("Area of circle =", area)

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
print("Area of rectangle =", area)

P = float(input("Enter principal: "))
R = float(input("Enter rate: "))
T = float(input("Enter time: "))

SI = (P * R * T) / 100
print("Simple Interest =", SI)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)

if b != 0:
    print("Division =", a / b)
else:
    print("Division not possible (division by zero)")


#code program for number comparison, grading system, and decision making if-elif-else.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print("First number is greater")
elif a < b:
    print("Second number is greater")
else:
    print("Both numbers are equal")
    
      
marks = float(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")


num = float(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")


#generate Multiplication table and compute sequence sums using while loops.
    
num = int(input("Enter a number: "))

i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1

n = int(input("Enter value of n: "))

i = 1
total = 0

while i <= n:
    total += i
    i += 1

print("Sum =", total)


#implement programs such as factorial calculation using while loop.

n = int(input("Enter a number: "))

fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

print("Factorial =", fact)


#write a program to determine whether a number is even or odd,

num=int(input("enter any number: "))
if num % 2 == 0:
    print("the number is even")

else:
    print("the number is odd")
