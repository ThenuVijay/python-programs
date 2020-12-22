done=0
total=int(input("Enter total:"))
while done==0:
    if 500>total>400:
       tamil=int(input("Enter tamil mark:"))
       if tamil>80:
           print("very good")
       else:
           print("Nice")
       done=1
    elif total > 500:
        print("total is greater than 500")
        print("enter lesser total")
        total=int(input("enter total")
        