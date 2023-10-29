# part 4

# b)

m = int(input('Give me number between 1 and 10: ')) 
if m>=1 and m<=10:
    print('Well done! You gave me: ', m) 

# d)

mark=float(input('Enter marks:'))
if mark < 0 or mark > 100:
    print('mark is invalid')
elif mark >= 70:  
    print('Exceptional result!') 
elif mark >= 40: 
    print('Satisfactory result!') 
else: 
    print('You have failed.') 

# f)

x = 10 
if not x > 10: 
    print("not returned True") 
else: 
    print("not returned False") 
