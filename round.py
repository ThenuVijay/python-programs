print(round(123.45))
print(round(100.254565,1))
print(round(100.756483,2))
print(round(129.9))


#divisors of given number


no=int(input("Enter num:"))
i=no
while i>1:
    if no%i==0:
        print(i)
    i-=1
    
no=int(input("Enter num:"))
i=2
while i<=no:
    if no%i==0:
        print(i)
    i+=1   