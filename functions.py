#Defining_function_1
def saif():
    print("I am studing at CSE.")
    print("My home district is Rajbari.")
saif()

#Argument_2
def greet(x,y): # this is paramater
    print(f"I am {x} {y}")
    print("I am very weak of python programming")
greet("TANJIB","SAIF")
greet("Umme","Ayesha") # this is actual value means Argument.

#Type_of_function_3
#1-Perform a task
#2-Return type
def greet(name):
    print(f"i am {name}")
    return "0000"
print(greet("saif"))

#Keyword_Argument_4
def increament(number,by):
    return number//by
print(increament(12,by=2))

# Defualt_Argument_5
def increament(first,secound,last=1):
    return (first+secound+last)
print(increament(10,9))

#xargs_6
def multiply(*numbers):
    total=1
    for number in numbers:
        total*=number
    return total
print(multiply(6,2,3))
print("All,okay")

#xxargs_7
def save_user(**user):
    print(user)
save_user(id=12345,name='Tanjib',age='19')

#Scope_8
message="a" #global_variable
def greet(name):
    global message # here the global variable is called.
    message="c" #local_variable
    #print(message)
greet("saif")
print(message)

#Excersice/Solution_13
def tanjib_saif(num):
    if (num%5==0) and (num%4==0):
        return "Tanjib Saif"
    elif num%5==0:
        return "Tanjib"
    elif num %4==0:
        return "Saif"
    # elif (num%5==0) and (num%4==0):
    #     return "Tanjib Saif"
    return num
print(tanjib_saif(12))

