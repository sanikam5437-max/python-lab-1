n = int(input("Enter a number: "))
fact = 1
temp = n

while temp > 0:
    fact *= temp
    temp -= 1

print(f"The factorial of {n} is {fact}")
