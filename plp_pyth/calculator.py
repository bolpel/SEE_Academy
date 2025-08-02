#this program will perform basic calculation
# base on user input

#prompt for first number
num1 = int(input("Enter your first number: "))
#prompt for second number
num2 = int(input("Enter your second number: "))

#prompt for operator
operator = input("Enter operator: ")

#display result
if operator == '+':
  res = num1 + num2
elif operator == '-':
  res = num1 - num2
elif operator == '*':
  res = num1 * num2
elif operator == '/':
  res = num1 / num2
else:
  print(f'You have entered invalid operator [{operator}]')

print(f'{num1} {operator} {num2} = {res}')