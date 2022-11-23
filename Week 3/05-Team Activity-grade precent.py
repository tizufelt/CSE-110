"""
TIM ZUFELT
CSE - 110 
Python FLow Control (if-else)
L05-Team-Activity
"""


print()
grade_precent = int(input("What is your grade precent? "))

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

if grade_precent >= 70:
    print("Way to go... you passed the class! ")

else:
    print("keep on, keeping on!")
    
    
