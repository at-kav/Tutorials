# part 6

# a)

n = input('Give me a number over 100:  ') 
try:
    n = int(n)
    if n <= 100: 
        print(n, 'is not over 100')  
except ValueError:
    print('Enter a integer value')

# b)

age = input('Enter your age:  ') 
try:
    age = int(age) 
    if age >= 18: 
        print("You can vote")
except ValueError:
     print('Enter a integer value')

# c)

num1=float(input('\nEnter Number 1:'))
operator=input('Enter "+","-","*","/" operator:')
num2=float(input('Enter number 2: '))

if operator == '+':
    print(num1+num2)
elif operator == '-':
    print(num1-num2)
elif operator == '*':
    print(num1*num2)
elif operator == '/':
    try:
        print(num1/num2)
    except ZeroDivisionError:
        print('Value divide by zero is infinity')
else:
    print('Invalid operator')


