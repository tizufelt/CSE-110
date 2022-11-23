"""
TIM ZUFELT
CSE - 110 
Python FLow Control (if-else)
L05-Prepare-Checkpoint
"""

print("Enter your name. ")
name = input().capitalize()

question = input(f"Hello {name} do you want to play a game? YES or NO... ")
print()
if question.lower().strip() == "yes":
    print("You are standing in the cavern of the Evil Wizard. All around you are the carcasses of slain ice dwarfs, what do you do? ")
    
  
    question = input("FIGHT, HIDE or PLAN YOUR ATTACK: ").lower().strip()
    if question == "fight":
        question = input("What weapon will you use? SWORD or STAFF ? ")
        if question == "sword":
            print("Hurray, you slay the Evil Wizard with your flaming sword. ALL IS SAVED!!!")
        
        elif question == "staff":
            print("You swing your staff at the  Evil Wizard and it breaks in two. The Evil Wizard casts a spell and freezes you. Sorry you lost. ")
        
        else:
            print("you hesitated and the Evil Wizard freezes you, Sorry you LOSE! ")
    elif question == "hide": 
        question = input("Where do you hide? BEHIND DOOR or BEHIND CURTAIN ? ").lower().strip()
        if question == "behind curtain":
            print("The Evil Wizard sees your feet from below curtain  and and casts a spell to freeze you in place. Sorry you lose!. ") 
            
        elif question == "behind door":
            question = input("The wizard walks by never noticing you, What do you do FIGHT or HIDE? ")
            if question == "fight":
                question = input("What weapon will you use? SWORD or STAFF ? ")
                if question == "sword":
                    print("Hurray, you slay the Evil Wizard, all is saved!!! ")
                elif question == "staff":
                    print("You swing your staff at the  Evil Wizard and it breaks in two. The Evil Wizard casts a spell and freezes you. Sorry you lost. ")
            else:
                print("You stay put trying to hide but the Evil Wizard spots you and casts a freezing spell locking you a block of ice forever. Sorry you lost! ")
    elif question == "run":
        question = print("The Evil Wizard is scarier than you expected. You turn and run away. This brings shame to you and the villagers lynch you. Sorry you lose! ")
    
    
    else:
        print("You hesitated to make a choice and the Evil Wizard froze you, Sorry... ")

else:
    print(" maybe next time then... Goodbye.  ")    

print()



 