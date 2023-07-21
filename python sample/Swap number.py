#Swap number using third variable.
x=int(input('Enter number 1:  '))
y=int(input('Enter number 2: '))
temp=x
x=y
y=temp
print('After swapping \nNumber 1: ',x)
print('Number 2: ', y)

#Swap number without using third variable.
x=int(input('Enter number 1:  '))
y=int(input('Enter number 2: '))
x,y=y,x
print('After swapping \nNumber 1: ',x)
print('Number 2: ', y)

