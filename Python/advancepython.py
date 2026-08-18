#decorator
"""
class Animal:
    @property
    def show(self):
        print("hello how are you ")

obj = Animal()
obj.show


"""
"""def decorate(func):
    def wrapper(*args):
        print("I will print myself before the function")
        func(*args)
        print("I will print after the funciton")
    return wrapper

@decorate

def addition(*args):
    sum =0
    for i in args:
        sum+=i
    print(F"total is {sum}")


addition(12,67)
"""
"""def decorate(func):
    def wrapper(*args):
        print("I will print myself before the function")
        func(*args)
        print("I will print after the funciton")
    return wrapper

@decorate

def information(**kwargs):
    for i in kwargs:
        print(f"{i}:{kwargs[i]}")



information(name = "Akarsh",age = 23, designation ="Ai/ml" )

"""
l= [i for i in range (1,21) if i%2==0]
print(l)