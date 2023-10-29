# Exercise 2

total = 0    # sum of scores 
count = 0    # number of scores entered 
                                                                 
# get one score & convert string to integer 
score = int(input("Enter score, (Enter -9 to end): ") )    
  
# Add while loop here. Loop while score is not -9
while score != -9:
    total += score   # Add score to total 
    count +=1        # Keep a count of scores
    score = int(input("Enter score, (Enter -9 to end): "))  # Get next score input 

#Ensuring at least one value has bean enterd
if count == 0:
    print('No scores have entered')
else:
    # print average of scores entered 
    average = float( total ) / count 
    print("Class average is", average)
 