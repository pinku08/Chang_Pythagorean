name=input('What is you name?:')

print ("Hello " + name)


print("Input lengths of shorter triangle sides:")
#Input length for a and b to find what c is.

a = float(input("a: "))
b = float(input("b: "))

 #calculates for c
c = (a**2 + b**2)**(1%2)

print('The length ' + str(c) + ' is the hypotenuse!!' )
