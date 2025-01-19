#conditional_statement_2
temperator=50
if temperator>30:
    print("Yah.It's true!")
    print("Let's go.")
#elif temperator>20:
    #print("Please give me a glass of water?")
else:
    print("The condition is wrong.")
print("Okay! Done")

#Ternary_operator_3
age=20
#if age>=18:
    #massege="Eligible"
#else:
    #massege="Not eligible."
massege="Eligible" if age>=18 else "Not eligible" #gudgment ternary.
print(massege)

#Logical_operator_4
high_income=False
good_credit=True
student=False
if (high_income or good_credit) and not student:  #gudgment logic.
    print("Eligible")
else:
    print("not eligible.")

#Chaining_comparison_Operator_6
age=23
#if age>=18 and age<65:  #age should be between 18 from 65.
if 18<=age <65:
    print("responsiblity")

#for_loop_8
for number in range(10):
    print("I love my Abbu & Ammu.",number+1,(number+1)*"#","@")

#for...else_9
amir_master=False
for number in  range(3):
    print("attempt")
    #if not amir_master:
    if amir_master:
        print("Yah!He is a master.")
        break
else:
    print("attempted 3 time and failed")

#Nested_loop_10
for i in range(5):
    for j in range(3):
       # for k in range(2):
        print(f"({i},{j})")

#Iterable_11
#for x in "Tanjib_Saif":
 #   print(x)
for item in "shopping_cart":
    print(item)
for i in ["S","A","I","F"]:
    print(i)

#while_loops_12
number=120
while number>0:
    print(number)
    number//=2
#command=""
#while command!="quit" and command!="QUIT":
 #   command=input("=")
  #  print("ECOAL",command)

#Infinity_loops_13
#command=""
#while True:
 #   command=input(">")
  #  print("ECO",command)
  #  if command.lower()=="quit":
   #     break

#Exercise_14
count=0
for number in range(1,20):
    if number%2==0:
        count+=1
        print(number)
print(f"We have {count}(1 between 20) even number.")