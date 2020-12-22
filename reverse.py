# reverse a number
num=input("Enter num: ")
i=len(num)-1
while i>=0:
    print(num[i],end=' ')
    i-=1


# Addition of digits
# 4 3 2 1--->4+3+2+1=10
num=input("Enter num: ")
sumofdigits=0
i=len(num)-1
while i>=0:
    sumofdigits=sumofdigits+int(num[i])
    i-=1
print(sumofdigits)    