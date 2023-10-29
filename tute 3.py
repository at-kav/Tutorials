n = input('Give me a number over 100: ')
try:
    n = int(n)
    if n <= 100:
        print(n, 'is not over 100')
    else:
        print(n, 'is over 100')
except ValueError as e:
    print(e.args[0])
    print('Please Enter a Number')