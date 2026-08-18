print("Namaste yt ")
#This is a comment
""" This is a multi line comment"""
#variables
sher = "nikhil"
a = 10
print(type(a))
v =23j
print(type(v))
v = "nikhil"
print(v)


#unicode and chr 

a = "A"
print(ord(a))

b =66
print(chr(b))

i = "nikhil"
print(i[0])


#slicing 
a= "Sher Coder"
print(a[5::1])

#type coversion

a = 10
a  = str(a)
print(type(a))



#input and output

age =int(input("Hello what is ur age"))
print (age)

#Operators


"""Arithmetic operator"""
a  =10
b =5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)



""" Assignment operator"""
a =  50
b = 10
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b
print(a)

"Comparison Operator "
print(a>b)
print(b<a)
"""print("a">a)"""# we cant compare string with an integer


"""Logical operator """

print(123>100 and 34==34 and 45<90 and 12>20)
print(12!=12 or 23==45 or 67 ==56 or 10>5)



"""Conditional statements """


a = 2

if a>10:
    print("Hello")
else:
    print("world")


age = int(input("Enter your age :"))

if age>18:
    print("You can vote")

elif age ==18:
    print("You Can also vote")
else:
    print("grew up first")