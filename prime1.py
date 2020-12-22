#no=13
#div=2
#no%div==0
#not prime
#div=div+1

no=int(input("Enter no:"))
div=2
while div<no:
    if no%div==0:
        print("Not prime")
        break
    div=div+1 
else:
     print(prime)