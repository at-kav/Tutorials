# Exercise 9

while True:
    choice=input("Choose menu options using numbers 1, 2, 3 and 4 and use option 4 to quit the program : ")
    try: 
        choice=int(choice)
    except ValueError:
        print('Enter Integer')
        continue

    if choice == 1:
        print('1 selected')
        break
    elif choice == 2:
        print('2 selected')
        break
    elif choice == 3:
        print('3 selected')
        break
    elif choice == 4:
        print('Quit selected')
        break
    else:
        print('Option not recognized')
