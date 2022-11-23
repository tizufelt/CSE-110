"""
Tim Zufelt
Input Output Data
CSE-110
L02-Team Activity
"""

#need this for the date that is auto populated
import datetime

#basic first step and variables
first_name = input("First Name: ")
last_name = input("Last Name: ")
email_address = input("Email Address: ")
phone_number = input("Phone Number: ")
job_title = input("Job Title: ")
id_number = input("ID: ")

#extra steps for stretched part
hair_color = input("Hair Color: ")
eyes = input("Eye Color: ")
date = datetime.date.today()
question = input("Have you been trained? Yes or No? ")


 #Print for the ID card and info
print()
print()
print()
print()
print("The ID card is: ")
print("-------------------------------------------")
print(last_name.upper() + ", " + first_name.capitalize())
print(job_title.capitalize())
print("ID:" + id_number)
print()
print(email_address)
print(phone_number)
print()
print("Hair: " + hair_color + "       " "Eyes: " + eyes + "   ")
print("Month:", date.strftime("%B") + "  Trained: " + question)
 
print("-------------------------------------------")
