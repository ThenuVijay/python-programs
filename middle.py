name=input("Enter your name:")
print(len(name))
mid=len(name)//2
print(name[0:mid]+name[mid].upper()+name[mid+1:])



name=input("Enter your name:")
print(len(name))
mid=len(name)//2
print(name[0:mid]+name[mid].lower()+name[mid+1:])


mark=90
if mark>=90:
    print("very good")
else:
    print("good")
    