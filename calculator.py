num1 = float(input("Enter your number: ")) or int(input("Enter your number: "))
operator = input("Enter your operator: ")
num2 = float(input("Enter your number: "))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
else:
    print("Invalid operator")