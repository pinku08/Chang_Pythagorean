a = int(input("please enter side a: "))
b = int(input("please enter side b: "))
c = int(input("please enter side c: "))


if (a**2 + b**2 == c**2):
    print('This is a right triangle!!!')
    
elif (a**2 + b**2 < c**2):
    print('This is an obtuse triangle!!!')
    
elif (a**2 + b**2 > c**2):
    print('This is an acute triangle!!!')

else:
    print('This is not a triangle!!!')
