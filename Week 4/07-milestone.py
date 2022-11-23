"""
Tim Zufelt 
Loops Part 1
CSE-110
L07 - Milestone Activity 
"""


def print_menu ():
    print("Lets play word-guess: ")
    print("Type a 5 letter word to guess: \n ")
    
    

print_menu()

def check_word():
  hidden_word = str("temple").lower()
  attempt = 6
  while attempt > 0:
    guess = str(input("Guess the word: ")).lower()
    if guess == hidden_word:
      print("You guessed the words correctly! ")
      break
    else:
      attempt = attempt - 1
      print(f"you have {attempt} attempt(s)  \n ")
 
      if attempt == 0:
        print(" Game over !!!! ")
  
check_word()



