num=int(input("Enter your number:"))
if num%2==0:
  print("It is even number")
else:
  print("It is odd number")
  
  
mark1=int(input("enter your mark:"))
mark2=int(input("enter your mark:"))
mark3=int(input("enter your mark:"))
if mark1>mark2 and mark1>mark3:
   print("mark1 is greater",mark1)
elif mark2>mark3:
   print("mark2 is greater",mark2)
elif mark1==mark2==mark3:
    print("all marks are same")
else:
   print("mark3 is greater",mark3)
 