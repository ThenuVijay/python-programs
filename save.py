#To get the marks and calculate total
subj=int(input("Enter total number of subjects: "))
i=0
tot=0
while i<subj:
    mark=int(input("Enter your mark : "))
    tot=tot+mark
    i=i+1
print("Your total marks  are",tot)


sent=input("Enter the sentence :")
i=0
count=1
length=len(sent)
while i<length:
    if sent[i]==' ':
        count+=1
    i=i+1
print(count)        
    

