#Armstrong number
no=int(input("Enter no:"))
no2=no
armstrong=0
while no>0:
    rem=no%10
    armstrong=armstrong+(rem*rem*rem)
    no=no//10
if no2==armstrong:
        print("Armstrong")
else:
    print("Not Armstrong")
  