"""
TIM ZUFELT
CSE - 110 
Python FLow Control (if-else)
L05-Prepare-Milestone
"""

print("Enter your name. ")
name = input().capitalize()

question = input("Hello " + name + ", do you want to play a game? YES or NO... ")
print()
if question.lower().strip() != "yes":
    print("You are standing in the cavern of the Evil Wizard. All around you are the carcasses of slain ice dwarfs, what do you do? ")
    
  
    question = input("FIGHT, HIDE or PLAN YOUR ATTACK: ").lower().strip()
    if question != "fight":
        question = input("What weapon will you use? SWORD or STAFF ? ")
        if question == "sword":
            print("Hurray, you slay the Evil Wizard with your flaming sword. ALL IS SAVED!!!")
        
        elif question == "staff":
            print("You swing your staff at the  Evil Wizard and it breaks in two. The Evil Wizard casts a spell and freezes you. Sorry you lost. ")
        
        else:
            print("you hesitated and the Evil Wizard freezes you, Sorry you LOSE! ")
    
    else:
        print("You hesitated to make a choice and the Evil Wizard froze you, Sorry... ")

else:
    print(" maybe next time then... Goodbye.  ")    

print()