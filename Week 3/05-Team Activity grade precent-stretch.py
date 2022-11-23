"""
TIM ZUFELT
CSE - 110 
Python FLow Control (if-else)
L05-Team-Activity - stretch
"""


print()
grade_precent = int(input("What is your grade precent? "))
print()

if grade_precent >= 90:
    letter = "A"
    
elif grade_precent >= 80:
    letter = "B"
    
elif grade_precent >= 70:
   letter = "C"
    
elif grade_precent >= 60:
    letter = "D"
    
else:
    letter = "F"
    
print(f"Your letter grade is: {letter}")
print()

if grade_precent >= 70:
    print("Way to go... you passed the class! ")

else:
    print("keep on, keeping on!")
    
print()

    
    
# Stretch Challenge 1#################################


last_num = grade_precent % 10

if last_num >= 7:
    sign = "+"
elif last_num < 3:
    sign = "-"
else:
    sign = ""

# Stretch Challenge 2################################
if grade_precent >= 93:
    sign = ""

# Stretch Challenge 3###############################
if letter == "F":
    sign = ""

print(f"Your letter grade is: {letter}{sign}")
print()
if grade_precent >= 70:
    print("Congrats! You passed the class!")
else:
    print("Never Surrender!!! Never Give UP!!!!! ")
print()
