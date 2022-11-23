"""
Tim Zufelt
Input Output Data
CSE-110
L02-Team Activity
"""




#My Birthday Script (to show addition and string)
first_num = input("How old are you? ")
display_age = int(first_num) + 1
print("On your next birthday, you will be " + str(display_age))
print()


#My Egg Carton Script (to show multiplication and string)
eggcarton = input("How many egg cartons do you have? ")
carton_num = int(eggcarton) * 12
print("You have " + str(carton_num) + " eggs total. ")
print()


#My Cookies Script (to show divide with user input)
cookies = int(input("How many cookies do you have? "))
people = int(input("How many people are there? "))
sharing = cookies / people
print(f"Each person may have {sharing} cookies")
print()
