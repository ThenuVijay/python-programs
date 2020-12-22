total=int(input("Enter total"))
while total>500:
    total=int(input("Enter total"))
    if total<=500:
        print(total)
        if total>400:
            tamil=int(input("Enter tamil mark"))
            if tamil>80:
                print("very good")
            else:
                print("Nice")
        else:
            print("ok thanks") 
    else:
       print("Total must be below 500")
            
            