"""
TIM ZUFELT
CSE - 110 
Python FLow Control (if-else)
L05-Prepare-Checkpoint
"""

print() #SPACE FOR START OF SCRIPT


firstnum = input("Enter a number between 1 and 100. ")
secondnum = input("Enter another number between 1 and 100. ")
print()
if firstnum > secondnum:
    print("the first number is greater ")
else:
    print("the first number is NOT greater ")
print()
############################################################    
if firstnum == secondnum:
    print("the numbers are equal ")
else:
    print("the number are NOT equal ")
print()
 ############################################################   
if firstnum < secondnum:
    print("the second number is greater ")
else:
    print("the second number is NOT greater")
print()
############################################################  

fav_animal = input("What is your favorite animal? ")
print()
if fav_animal.lower() == "lion":
    print("That's my favorite too! ")
else:
    print("sorry, but thats not my favorite. ")
print()

