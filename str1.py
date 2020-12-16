name=input('tell your name :')
print(name)
#print(name[0:-1] + name[-1])
#print(name[-5:-1])
print(name[0:5:2])
#print(name[0:4])
length=len(name)-1
middle=int(length/2)
print(name[middle].upper())
