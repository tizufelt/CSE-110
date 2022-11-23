"""
Tim Zufelt 
Loops Part 1
CSE-110
L08 - Milestone Activity 
"""


import random

def print_menu():
    print()
    print("Let's play Wordle:")
    print("Type a 5 letter word and hit enter!\n")

def check_word():
    hidden_word = ["apple", "house", "taxes", "clone", "atone", "pines"]
    secret = random.choice(hidden_word)
   
    attempt = 1
    max_tries = 7
    while attempt < max_tries:
        user_guess = str(input())
        
        if user_guess != secret:
            if len(user_guess) != 5:
                print("word must be 5 characters long, guess again! ")
            else:
                for i in range( min(len(user_guess.lower()), 5) ):
                    if user_guess[i] == secret[i]:
                        print(user_guess[i].upper(), end="")
                    elif user_guess[i] in secret:
                        print(user_guess[i].lower(), end="")
                    else:
                        print(" _ " ,end="")
                attempt += 1
                print()
                print()
               
        else:
            print(f"way to go! YOU WON in {attempt} moves! ")
            break
            
               
    print()

print_menu()
check_word()