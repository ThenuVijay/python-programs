total=int(input("Enter total:"))
while total>500:
    print("total is greater than 500")
    total=int(input("Enter total:"))
else:    
    if total>=400:
        tamil=int(input("Enter tamil mark:"))
        if tamil>80:
            print("very good")
        else:
            print("Nice")
    else:
        print("ok")

