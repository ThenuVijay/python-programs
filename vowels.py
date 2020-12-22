name=input("Name:")
length=len(name)

i=0
while i<length:
    #if name[i]=='a' or name[i]=='e' or name[i]=='i' or name[i]=='o' or name[i]=='e':
    if name[i] not in ['a','e','i','o','u']:
        print(name[i])
        
    i=i+1    
    
name=input("Name:")
length=len(name)
count=0
i=0
while i<length:
    #if name[i]=='a' or name[i]=='e' or name[i]=='i' or name[i]=='o' or name[i]=='e':
    if name[i] in ['a','e','i','o','u']:
        count+=1
        print(name[i])
        
    i=i+1    
print("no of vowels present are:",count)
       
       
name=input("Enter sentence:")
length=len(name)
count=1
i=0
while i<length:
    #if name[i]=='a' or name[i]=='e' or name[i]=='i' or name[i]=='o' or name[i]=='e':
    if name[i] ==' ':
        count+=1
        #print(name[i])
        
    i=i+1    
print("no of words present are:",count)
              