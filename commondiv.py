no1=int(input('Enter no:'))
no2=int(input('Enter no:'))
if no1<no2:
    small=no1
elif no2<no1:
    small=no2
print("Common divisors are")
while small>2:
        if no1%small==0 and no2%small==0:
            print("GCd",small)
            #break
        small-=1    
    
    