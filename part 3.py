# part 3

# a)

fahrenheit = 0
Celsius = 0
convertion=int(input('Enter 1 to covert Celsius to Fahrenheit or 2 to convert Fahrenheit to Celsius :'))
if convertion == 1:
    Celsius=int(input('Enter Celsius value : '))
    fahrenheit=(Celsius*1.8)+32
    print('Temperature in Fahrenheit is',fahrenheit)
elif convertion == 0:
    farenheit=int(input('Enter Farenheit value : '))
    Celsius=(fahrenheit*1.8)+32
    print('Temperature in Celsius is',Celsius)  
else:
    print('Invalid Option entered')

# b)

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
    if num2 == 0:
        print('Error')
    else:
        print(num1/num2)
else:
    print('Invalid operator')

# c)

cost=float(input('\nEnter the cost of meals:'))
satisfaction=int(input('''Enter satisfaction level
1 = Totally satisfied
2 = Satisfied
3 = Dissatisfied : '''))
if satisfaction == 1:
    tip = cost*20/100
    print('Totally satisfied \ntip amout=',tip)
elif satisfaction == 2:
    tip = cost*15/1001
    print('Satisfied \ntip amout=',tip)
elif satisfaction == 3:
    tip = cost*10/100
    print('Dissatisfied \ntip amout=',tip)

