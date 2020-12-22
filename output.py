a,b,c=100,200,300
print(a,b,c, sep=':')
print(a,b,c, end='-')


#Formatted string:
#%i --> int
#%d --> int
#%f -->float
#%s -->string


name='langscape'
print('Welcome to %s'%name)


a,b,c=100,200,300
print("a value %d"%a)
print("b value is %d and c is %d"%(b,c))

#Replacement Operator;
name='vishnu'
city='ooty'
print('Hi This is {}.I am from {}'.format(name,city))
print('Hi This is {0}.I am from {1}'.format(name,city))
print('Hi This is {1}.I am from {0}'.format(name,city))
#print('Hi This is {4}.I am from {5}'.format(name,city))