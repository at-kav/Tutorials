# Exercise 8

# a)

for number in range(3) :   
    print("-------------------------------------------") 
    print("Outer loop iteration " + str(number)) 
# Inner loop 
    for another_number in range(4):   
        print("****************************") 
        print("In inner loop iteration " + str(another_number))

# b)

for x in range(1,4):  # print 3 rows 
    for y in range(1,4):  # 3 asterisks a row 
        print('*', end='') 
    print()

# c)

for x in range(1,4):  # print 3 rows 
    print('*'*x) 
print() 