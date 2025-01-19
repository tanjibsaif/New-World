#Creating_classes_2
class Point:
    def draw(self):
        print("draw")
point=Point()
print(type(point))
print(isinstance(point,Point))


#Constructors_3
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def draw(self):
        print(f"This point is ({self.x} & {self.y})")

point=Point(33,54)
print(point.x)
point.draw()


#Class_vs_Instance_Attributes_4
class Point:
    defult_colour="Green"

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def draw(self):
        print(f"This point is ({self.x} & {self.y})")

Point.defult_colour="Yellow"

point=Point(33,54)
print(point.defult_colour)
point.draw()

another=Point(3,4)
print(another.defult_colour)
another.draw()


#Class_vs_instance_method_5
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    @classmethod
    def zero(cls):
        return cls(0,0)
    
    def draw(self):
        print(f"This point is ({self.x} & {self.y})")

point=Point.zero()
point.draw()


#Magic_method_6
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return f"(safwan {self.x},{self.y})"

    def draw(self):
        print(f"This point is ({self.x} & {self.y})")

point=Point(1,2)
print(str(point))


#Comparing_Object_7
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __gt__(self,other):
        return self.x>other.x and self.y>other.y
point=Point(10,20)
other=Point(1,2)
print(point>other)


#Arithmetic_Operation_8
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)

point=Point(10,20)
other=Point(1,2)
combined=point+other
print(combined.x)


#Custom_Containers_9
class Tagcloud:
    def __init__(self):
        self.tags={}

    def add(self,tag):
        self.tags[tag.lower()]=self.tags.get(tag.lower(),0)+1
    
    def __getitem__(self,tag):
         return self.tags.get(tag.lower(),0)
    
    def __setitem__(self,tag,count):
        self.tags[tag.lower()]=count
    
    def __len__(self):
        return len(self.tags)
    
    def __iter__(self):
        return iter(self.tags)       

cloud=Tagcloud()
cloud["SAIF"]=10
len(cloud)
cloud.add("saif")
cloud.add("saif")
cloud.add("saif")
cloud.add("saif")
print(cloud.tags)


#Private_Members_10
class Tagcloud:
    def __init__(self):
        self.__tags={}

    def add(self,tag):
        self.__tags[tag.lower()]=self.tags.get(tag.lower(),0)+1
    
    def __getitem__(self,tag):
         return self.__tags.get(tag.lower(),0)
    
    def __setitem__(self,tag,count):
        self.__tags[tag.lower()]=count
    
    def __len__(self):
        return len(self.__tags)
    
    def __iter__(self):
        return iter(self.__tags)       

cloud=Tagcloud()
print(cloud._Tagcloud__tags)


#Property_11
class Product:
    def __init__(self,price):
        self.price=price
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self,value):
        if value<0:
            raise ValueError("Price cannot be negative. ")
        self.__price=value
   
product=Product(40)
product.price=2
print(product.price)


#Inheritans_12
class Animal:
    def __init__(self):
        self.age=23
    
    def eat(self):
        print("eat")
#Animal is parent/supper class
#Mammal is Child/sub class     
class Mammal(Animal):
    def walk(self):
        print("walk")

class Fish():
    def swim(self):
        print("swim")
saif=Mammal()
saif.eat()
print(saif.age)


#The_Object_class_13
class Animal:
    def __init__(self):
        self.age=23
    
    def eat(self):
        print("eat")
     
class Mammal(Animal):
    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")
saif=Mammal()
tanjib=Fish()
print(isinstance(saif,Animal))
# print(issubclass(Fish,object))


#Method_Overriding_14
class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age=23
    
    def eat(self):
        print("eat")
    
# class Mammal(Animal):
#     def __init__(self):
#         super().__init__()
#         print("Mammal Consturctor")
#         self.weight=2
#         # super().__init__()
    
    
    def walk(self):
        print("walk")

class Fish(Animal):
    def __init__(self):
        # super().__init__()
        print("Fish Constructor")
        self.weight=3.45
        super().__init__()
    def swim(self):
        print("swim")


saif=Fish()
print(saif.age)
print(saif.weight)


#Multi_level_inheritance_15
class Bird:
    def eat(self):
       
        print("Eat")
    
class Crow(Bird):
    def fly(self):
        print("fly")

class Chichen(Crow):
    pass 

hen=Chichen()
hen.eat()
hen.fly()


#Multiple__inhetance_16
class Employee:
    def greet(self):
        print("Employee greet")
        
class Person:
    def greet(self):
        print("Person greet")
        
class Manager(Person,Employee):
    pass
     

manager=Manager()
manager.greet()


#Example_of_inheritance_17
class InvalidOperationError(Exception):
    pass
class Stream:
    def __init__(self):
        self.opened=False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is alredy open.")
        self.opened=True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is alredy close.")
        self.opened=False

class FileStream(Stream):
    def read(self):
        print("Reading data from a file.")

class FileNetwork(Stream):
    def read(self):
        print("Reading data from a network")

class Manager(FileStream,FileNetwork):
    pass
manager=Manager()
manager.read()

#Abstruct_Base_classes_18
from abc import ABC,abstractmethod

class InvalidOperationError(Exception):
    pass
class Stream(ABC):
    def __init__(self):
        self.opened=False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is alredy open.")
        self.opened=True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is alredy close.")
        self.opened=False

    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print("Reading data from a file.")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a  Network ")

class MemoryStream(Stream):
    def read(self):
        print("Reading data from Memory stream")

stream=NetworkStream()
stream.read()


#Polymorphism_19
from abc import ABC,abstractmethod

class Tanjib(ABC):
    @abstractmethod
    def draw(self):
       pass

class Saif(Tanjib):
    def draw(self):
        print("Saif..")

class Nishat(Tanjib):
    def draw(self):
        print("Nishat")

def draw(controls):
    for control in controls:
        control.draw()

n=Nishat()
# print(isinstance(n,Tanjib))
s=Saif()
draw([n,s])


#Duck_Typing_20
from abc import ABC,abstractmethod

class Saif:
    def draw(self):
        print("Saif..")

class Nishat:
    def draw(self):
        print("Nishat")

def draw(controls):
    for control in controls:
        control.draw()

n=Nishat()
# print(isinstance(n,Tanjib))
s=Saif()
draw([n,s])


#Extending_Built_in_type_21
class Text(str):
    def duplicate(self):
        return self+self+self

# text=Text("TAnjib saif")
# print(text.lower())

class TrackableList(list):
    def append(self,object):
        print("Append called")
        super().append(object)

list=TrackableList()
list.append("w")


#Data_Classes_22
from collections import namedtuple

Point=namedtuple("Point",["x","y"])
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

#     def __eq__(self, other):
#         return self.x==other.x and self.y==other.y
p1=Point(x=1,y=2)
p3=Point(x=10,y=2)
p2=Point(x=1,y=2)
print(p1==p2)