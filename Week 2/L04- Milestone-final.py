"""
Tim Zufelt
Input Output Data
CSE-110
L02-Team Activity
"""


print()
print("############## Your TIP Calculator ##############")
print()
#cost of meals from users
child = float(input("What is the price of a child's meal? "))
adult = float(input("What is the price of an adult's meal? "))

#number of users 
child_num = int(input("How many children are there? "))
adult_num = int(input("How many adults are there? "))

#tax rate for cost of meals
tax = float(input("What is the sales tax? "))
#WhiteSpace
print()

#outputs for fist part of calculations
subtotal = child * child_num + adult * adult_num
tax= subtotal * tax * .01
total = subtotal + tax

#print statements for calculations
print(f"Subtotal: ${subtotal:.2f}")
print(f"Sale Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
#whitespace
print()

#script for TIP to be added 
tip = input("Would you like to leave a tip? 10%, 15%, or 20% ? ")
if tip ==("20"):
    print(f"Tip Amount: ${.20 * total:.2f}")
    outcome = float(round(total * .20, 2))
if tip ==("15"):
    print(f"Tip Amount: ${.15 * total:.2f}")
    outcome = float(round(total * .15, 2))
if tip ==("10"):
    print(f"Tip Amount: ${.10 * total:.2f}")
    outcome = (round(total * .10, 2))
#new total plus tip to show user
print(f"New Total: ${total + outcome:.2f}")
#whitespace
print()

#output for paymenty and change calculations
payment = float(input("What is the payment amount? "))
change =  float(payment - (total + outcome))

#final cost back in change
print(f"Change Amount: ${change:.2f}")
print()