#List_1
letters=["a","b","c"]
print(letters)
matrix=[["a","b"],["c","d"]]
print(matrix)
char=letters+matrix
print(char)
char=list(range(10))
print(char)
char=("I am tanjib saif.I am a beginners.")
print(len(char))

#Accessing_items_2
letters=["a","b","c","d"]
print(letters)
letters[0]="A"
print(letters)
print(letters[::3])

numbers=list(range(20))
numbers[3]=24
print(numbers)
print(numbers[::-1])

#List_Unpacking_3
numbers=["SAIF","SHAKIL","TASMIA","UMARA","SAFWAN"]
print(len(numbers))
first,secound,*other,last=numbers
print(first,secound)
print(last)
print(other)


#Looping_Over_List_4
letters=["a","b","c"]
items=(0,"a")
index,letter=items
for index, letter in enumerate(letters):
    print(index,letter)

#Item_Add/remove_5
letters=["a","b","c"]
#add
letters.append("d")
letters.insert(1,"__")
print(letters)
#remove
letters.pop(1)
letters.remove("d")
del letters[-3]
print(letters)

#Finding_items_6
val=["saif","safwan","ayesha"]
print(val.count("ummara"))
if "ummara" in val:
    print(val.index("ummara"))


#Sorting_list_7
# numbers=[34,65,1,4]
# # numbers.sort(reverse=True)
# print(sorted(numbers,reverse=True))
# print(numbers)
items=[
    ("product1",5),
    ("product2",1),
    ("product3",23),
    ("product4",2),
]
def sort_items(item):
    return item[1]

items.sort(key=sort_items)
print(items)


#Lamdas_8
items=[
    ("product1",5),
    ("product2",1),
    ("product3",23),
    ("product4",2),
]
# def sort_items(item):
#     return item[1]
items.sort(key=lambda item:item[1])  #syntax of lamda func parametters:Expresion
print(items)


#map_function_9
items=[

    ("product1",5),
    ("product2",1),
    ("product3",23),
    ("product4",2),]
price=[]
for item in items:
     price.append(item[1])

price=list(map(lambda item:item[1],items))
# for item in price:
#     print(item)
print(price)


#Filter_function_10
items=[

    ("product1",10),
    ("product2",20),
    ("product3",7),
    ("product4",2),
]
filtered=list(filter(lambda item:item[1]>=7, items))
print(filtered)


#List_Comprehension_11
items=[

    ("product1",10),
    ("product2",20),
    ("product3",7),
    ("product4",2),
]
# price=list(map(lambda item:item[1],items))
price=[item[1] for item in items]
print(price)
# filtered=list(filter(lambda item:item[1]>=7, items))
filtered=[item for item in items if item[1]>10]
print(filtered)


#Zip_function_12
list_1=[4,7,10,13]
list_2=[5,8,11,14]
list_3=[6,9,12,15]
print(list(zip("SAIF",list_1,list_2,list_3)))


#Stacks_13
browsing_session=[]
browsing_session.append(1) 
browsing_session.append(2)
browsing_session.append(3)
browsing_session.append(4)
print(browsing_session)
last=browsing_session.pop()
print(last)
print(browsing_session)
print("minus",browsing_session[-1])
if not browsing_session:
    print("saif")


#Queues_14
from collections import deque
Queue=deque([])
Queue.append(1)
Queue.append(2)
Queue.append(3)
Queue.popleft()
print(Queue)
if not Queue:
    print("emt")

#Tuple_15
point=(1,2,10)
print(point[0:-1])
x,y,z=point
if 10 in point:
    print("exit") 

#Swapping_16
x="Tanjib"
y="Saif"
x,y=y,x

z=x
x=y
y=z
print("x",x,"y",y)
print(x,y)


#Arrays_17
from array import array
numbers=array("i",[1,2,3])
numbers[0]=4
print(numbers)

#Sets_18
numbers=[1,2,3,6]
first=set(numbers)
print(first)
secound={1,2,4,5,6}

print(first|secound)
print(first & secound)
print(first - secound)
print(first ^ secound)

if not 7 in first:
    print("yes")


#Dictionarice_19
name={"A":1,"B":2}
point=dict(A=1,B=4)
print(point)
point["A"]=10
point["C"]=30
print(point)
if "a" in point:
    print(point["a"])
print(point.get("a",40))
del point["C"]
print(point)
for key in point:
    print(key,point[key])


#Dictionary_Comprtehensions:
# values={}
# for x in range(5):
#     values[x]=x*2
# print(values)
values={x:x*2 for x in range(5)}    # dict_comprehensions syntax is {expresions for item in items}
print(values)


#Generator_Expresions_21
from sys import getsizeof
values=(x*2 for x in range(100000))
print("gen:",getsizeof(values))

values=(x*2 for x in range(100000))
# print("list:",getsizeof(values))
# print(len(values))


#Unpaking_Operator_22
# nums=[1,2,3,4]
# print(*nums)
# print(1,2,3)
values=list(range(5))
values=[*range(5),*"HELLO"]
print(values)
x=[1,2,3]
y=[1,2]
val=[*x,*y,*"Hello"]
print(val)

first={"v":111,"w":222}
secound={"x":333}
combined={**first,**secound,"y":444}
print(combined)


#Exercise_23
from pprint import pprint
sentence="Hello I am Tanjib Saif I am Studying CSE at Faridpur Polythecnic Institute My dream is to become an AI Consultrant"
char_friquency={}
for i in sentence:
    if i in char_friquency:
        char_friquency[i]+=1
    else:
        char_friquency[i]=1
char_friquency_sorted=sorted(
    char_friquency.items(),
    key=lambda kv:kv[1],
    reverse=True)
print(char_friquency_sorted[0])
