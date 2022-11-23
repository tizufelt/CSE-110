while True:
     choices = input("Can I have a piece of candy?  ")
     if (not choices in ["yes", "sure", "maybe"]):
         continue
  
     else:
         print("Thank you! ")
         break