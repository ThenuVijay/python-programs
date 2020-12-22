no=1
while no<=5:
    print(no,' * 5 =',no*5)
    no+=1
    
    
no=1
while no<=5:
    print(no,' * 5 =',no*5)
    no+=1 
    
#Total marks program
subjects=int(input("enter no. of subjects"))
sub2 = subjects
total=0
while subjects>0:
        mark=int(input("enter mark"))
        total=total+mark
        subjects-=1
print("Total is",total)
print("percentage is",total//sub2)#round(total/sub2,2).it will round of the digits to 2 like 98.45