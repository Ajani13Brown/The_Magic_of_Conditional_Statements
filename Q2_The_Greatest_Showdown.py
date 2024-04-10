# Task 1: Identify the Greatest

num_1 = int(input ("Choose a number: "))
num_2 = int(input("choose a second number: "))
num_3 = int(input ("choose a third number: "))
if num_1 > num_2 and num_3:
     print (num_1, "is the largest")
elif num_2 > num_1 and num_3:
     print (num_2, "is the largest")
elif num_3 > num_2 and num_1:
    print (num_3, "is the largest")
    
# Task 2: Identify the Smallest

if num_1 < num_2 and num_3:
     print (num_1, "is the smallest")
elif num_2 < num_1 and num_3:
     print (num_2, "is the smallest")
elif num_3 < num_2 and num_1:
    print (num_3, "is the smallest")