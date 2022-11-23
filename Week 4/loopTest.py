
import random

def processGuess(theAnswer, theGuess):
    position = 0
    clue = ""
    for letter in theGuess


def print_menu ():
    print("Lets play word-guess: ")
    print("Type a 5 letter word to guess: \n ")
    

word_list = ["temple", "nephi", "mosiah", "house", "pickle"]

answer = random.choice(word_list)

number_of_guesses = 0
guessed_correctly = False

while number_of_guesses < 6 and not guessed_correctly:
    guess = input("Type in a 5 letter word and press enter: ")
    print("you have a guess", guess)
    number_of_guesses += 1