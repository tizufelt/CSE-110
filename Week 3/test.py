
from random import choices


import random


#if today == input():
#	print('Your weekend is over. Go to work.')
#elif today=='Sunday' or today=='Saturday':
#	print('Today is off.')
#else:
#	print('Go to work.')
 
while True:
    choices = input("Enter rock, paper, scissors: ")
    if (not choices in ["rock", "paper", "scissors"]):
        print("Please enter proper choice")
        continue
  
    else:
        break


     
 