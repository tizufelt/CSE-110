
import random
import sys

def print_welcome():
    print("Lets play word-guess: ")
    print("Type a 5 letter word to guess: \n ")
    

def wordle_word():
    hidden_word = ["apple", "house", "temple", "clone", "atone,"]
    return random.choice(hidden_word)

print_welcome()
userword = input()

for letter in range( min(len(userword), 5) ):
    if userword[i] == wordle_word[i]:
        print(userword[i].upper(), end="")
    elif userword[i] in wordle_word:
        print(userword[i].lower(), end="")
    else:
        print("_" ,end="  ")

        if userword == wordle_word:
            print("WAY TO GO!")

        else:
            print("Sorry too bad")
    
     


