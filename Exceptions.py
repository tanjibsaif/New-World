#Handiling_Exception_2
try:
    age=int(input("age:"))
except ValueError as ex:
    print("you don't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print("Okay!But it is true.")
print("Now is All okay")


#Handiling_different_Ex_3
try:
    age=int(input("age:"))
    xfactor=10/age
except (ValueError,ZeroDivisionError):
    print("you don't enter a valid age.")
# except ZeroDivisionError:
#     print("you don't enter a valid age.")
else:
    print("Okay!But it is true.")
print("Now is All okay")


#Cleaning_Up_4
try:
    file=open("Exceptions.py")
    age=int(input("age:"))
    xfactor=10/age
except (ValueError,ZeroDivisionError):
    print("you don't enter a valid age.")
else:
    print("Okay!But it is true.")
finally:
    file.close()

#The_with_Statement_5
try:
    with open("with.py") as file:
        print("file opend")
    age=int(input("age:"))
    xfactor=10/age
except (ValueError,ZeroDivisionError):
    print("you don't enter a valid age.")
else:
    print("Okay!But it is true.")
# finally:
#     file.close()


#Raising_Exceptions_6
def __saif__(age):
    if age >0:
        raise ZeroDivisionError("Age cannot be 0 or less.")
    return 10/age
try:
    __saif__(1)
except ZeroDivisionError as error:
    print(error)


#Cost_of_raising_Ex_7
from timeit import timeit
code1="""
def __saif__(age):
    if age >0:
        raise ZeroDivisionError("Age cannot be 0 or less.")
    return 10/age
try:
    __saif__(1)
except ZeroDivisionError as error:
    pass
"""
code2="""
def __saif__(age):
    if age >0:
        return None
    return 10/age

xfactor=__saif__(1)
if xfactor==None:
    pass
"""
print("first code",timeit(code1,number=100000))
print("secound code",timeit(code2,number=100000))
































