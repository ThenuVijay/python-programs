#no=13
# 13%2==0
# not prime
# 13%3==0
# not prime
# 13%4==0
# not prime
# 13%5==0
# not prime

# ........13%13==0


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
     print("prime")