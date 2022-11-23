"""
Tim Zufelt
Input Output Data
CSE-110
L02-Prove Assignment MadLIB
"""


#USER INPUTS INFO
adjective = input("please enter in an adjective. ")
animal = input("please enter in an animal name. ")
first_verb = input("please enter in a verb. ")
exclamation = input("please enter in an exclamation word. " )
second_verb = input("please enter in another verb. ")
third_verb = input("please enter in one more verb. ")


#Final Sentence
output = f"The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {first_verb} down the hallway. {exclamation.capitalize()}, I yelled! But all \
I could think to do was to {second_verb} over and over. Miraculously, that caused it to stop, but not before it tried to {third_verb} right in front of my family. "

#spaces used
print()
print()
print()

print(output)

