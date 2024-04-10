year = int(input("Enter Year: "))

if year % 4 ==0 and not year % 100 == 0:
    print("Yep! thats a Leap Year!")
elif year % 4== 0 and year % 400 == 0:
   print("Yep! thats a Leap Year!")
else:
    print("Nope, Not a Leap Year.")