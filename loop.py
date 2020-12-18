count=0
while count<5:
    print(1)
    count=count+1
    
count=0
while count<5:
    print(count)
    count=count+1    
       
count=1
while count<=5:
    print(count)
    count=count+1       
       
count=10
while count>=1:
    print(count)
    count=count-2    
  
count=1
while count<=10:
    print(count,sep=' ')
    count=count+2   

# 2 4 6 8......  
count=1
maxno=int(input("Enter maximum number"))
while count<=maxno:
    print(count, end=' ')
    count+=2
    
#3 6 9 12 15.....
count=3
maxno=int(input("Enter maximum number"))
while count<=maxno:
    print(count, end=' ')
    count+=3  #count=count+3 
 

#multiples of 3 
count=3
maxno=int(input("Enter maximum number"))
while count<=maxno:
    print(count, end=' ')
    count+=3  #count=count+3 
       
start=1
while start<=20:
        if start%3==0:
            print(start)
        start+=1    

#outputs are same but below pgm is the best because of less count of looping    
start=3
while start<=20:
        print(start)
        start+=3
        
#multiples of 2 and 3
start=1
while start<=100:
        if start%3==0 and start%2==0:
            print(start)
        start+=1    
        
        
   
start=1
while start<=100:
        if start%3==0 or start%2==0:
            print(start)
        start+=1    
        