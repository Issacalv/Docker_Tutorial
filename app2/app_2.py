import math

print("Input two numbers to add together")


print("Enter the first number: ")
first_num = float(input())

print("Enter the second number: ")
second_num = float(input())

try:
    print(f"{first_num} + {second_num} = {first_num + second_num}")
except:
    print("Incorect input format")