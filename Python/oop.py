"""class Factory:
    def __init__(self,material,zips,pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets 
    def show(self):
        print(f"your object details are {self.material},{self.pockets},{self.zips}")

reebok = Factory("leather",3,2)
campus = Factory("nylon",3,3)

reebok.show()

class animal:
    name = "lion"


    def __init__(self,age):
        self.age = age

    @classmethod

    def hello(cls):
        print("this is  a class method")"""
# inheritance
"""class factory:
    a =12
    def hello(self):
        print("Class is factory")

class factory2(factory):
    pass

obj =factory()
obj.hello()

obj2 = factory2()
print(obj2.a)
"""

"""class Animal:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"Hello your name is {self.name},{self.age}")

class human(Animal):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

animal1 = Animal("Lion")
person1 =human("AKARSH",23)

person1.show()"""


"""class animal:
    name1 = 'Lion'

class Human:
    name2 = "Harsh"

class Robots(animal,Human):
    name3 = "charlie123"

obj = Robots()

print(obj.name1)"""


"""class Factory():
    def __init__(self,material,zips):
        self.material = material
        self .zips= zips



class BhopalFactory(Factory):
    def __init__(self,material,zips,color):
        super().__init__(material,zips)
        self.color = color

class PuneFactory(BhopalFactory):
    def __init__(self,material,zips,color,pockets):
        super().__init__(material,zips,color)
        self.pockets = pockets

obj = PuneFactory("POLYSTER",4,"BLACK",5)
print(obj.material)

"""

#polymorphism
#method overriding
"""class Animal:
    def show(self):
        print('hello i am akarsh')

class Human(Animal):
    def show(self):
        print("How are you")

obj = Human()
obj.show()"""

#duck typing
"""
class Animal:
    def show(self):
        print("I am showing")

class Human:
    def show(self):
        print("I  am also showing")

obj =Animal()
obj1 = Human()

obj.show()
obj1.show()"""



# encapsulation

"""class Factory:
    __a = "pune"

    def show(self):
        print("hello i am factory")



class Bhopal(Factory):
    def show2(self):
        print(super().__a)
obj = Bhopal()
obj.show2()"""


#abstraction
"""from abc import ABC,abstractmethod

class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass

class Square(abstract):
    def __init__(self,side):
        self.side =side

class Circle:
    def __init__(self,radius):
        self.radius = radius


obj = Square()
print(obj.side)"""
"""from abc import ABC,abstractmethod

class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass

class Square(abstract):
    def __init__(self,side):
        self.side =side
    def perimeter(self):
        print("I HAVE CREATED ABSTRACT METHOD")
class Circle:
    def __init__(self,radius):
        self.radius = radius


obj = Square(5)
print(obj.side)
"""


class Animal:
    def __init__(self,name, age):
        self.name=  name
        self.age = age
    def __str__(self):
        return "hello how are you "
    def __add__(self,other):
        sum =0
        for i in other :
            sum = sum+i.age
        return f"{self.age +sum}"
obj = Animal("Lion",12)
obj1 = Animal("dog",56)
obj2 = Animal("Tiger",85)
print(obj+{obj1,obj2})