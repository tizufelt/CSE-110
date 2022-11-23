import random



hidden_word = ["apple", "house", "taxes", "clone", "atone", "pines"]
random_word = random.choice(hidden_word)

def print_menu():
    print("Let's play Wordle:")
    print("Type a 5 letter word and hit enter!\n")


print_menu()

for attempt in range(1, 7):
        user_guess = input().lower()
        for letter in range( min(len(user_guess.lower()), 5) ):
                if user_guess[letter] == random_word[letter]:
                        print(user_guess[letter].upper(), end="")
                elif user_guess[letter] in random_word[letter]:
                        print(user_guess[letter].lower(), end="")
                else:
                        print("_ " ,end="")
                print()       

                if user_guess == random_word:
                        print(f"CONGRATS YOU WON in {letter} moves! ")
                        break
                elif attempt == 6:
                        print(f"Sorry the wordle word was =  {random_word}")
                        break