no=0
while no<5:
     no=no+1
     if no==3:
        break
     print(no)
else:    
    print('exit')    

no=0
while no<5:
     no=no+1
     if no==3:
        break
     print(no)    
print('exit')  

emailid=input("enter mail id: ")
i=0
length=len(emailid)
while i<length:
    if emailid[i]>='0' and emailid[i]<='9':
        print(emailid[i],end=' ')
    i+=1



emailid=input("enter mail id: ")
i=0
length=len(emailid)
while i<length:
    if emailid[i]>='a' and emailid[i]<='z':
        print(emailid[i],end=' ')
    i+=1
      
    