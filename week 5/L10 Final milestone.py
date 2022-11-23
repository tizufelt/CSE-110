"""
Tim Zufelt 
Lists and loops 
CSE-110
L10 - Final Milestone
"""



cart = {}


def option_1():
    print()
    item = input(" What would you like to add?  ")
    price = float(input(" type in the price: "))
    print()
    cart [item] = price
    print(f"'{item.upper()}' has been added to your cart.")
    print(f" The price is ${price:.2f}")
   
        
def option_2():
    print()
    print(f" You have {len(cart)} items in your shopping cart")
    print()
    for i, (item, price ) in enumerate(cart.items(), start=1):
        print(f"{i}. {item.upper()} - ${price:.2f}")
               
        
def option_3():
    takeout = input(" Type in what you would like to remove.  ")
    cart.pop(takeout)


def option_4():
    sum = 0
    for item in cart:
        sum += cart [item]
    print()
    print("Total Cart value is...")
    print(f" Total - ${sum:.2f}")


def option_5():
    print()
    print ("Thank you for shopping with us... Bye.")
       
    
def welcome_menu():
    print()
    print()
    print("#############################################\n"
          "###                                       ###\n"
          "###    Welcome to Your Shopping Cart      ###\n"
          "###                                       ###\n"
          "#############################################")
    print()


welcome_menu()    

while True:
    print()
    print ("Please choose from the menu below:")
    print()
    print ("1. Add item. ")
    print ("2. View cart. ")
    print ("3. Remove Item. ")
    print ("4 compute total.")
    print ("5. exit cart.")
    print()

    option = int(input("> "))
    if option == 1:#add item option
        option_1()
    
    if option == 2:#view option
        option_2()
        
    if option == 3:#remove option
        if cart:
            option_3()
        else:
            print("\n*** Your cart is empty... Please add an item. ***\n")
       
    if option == 4:#total cost option
        option_4()
        
    if option == 5:#exit program option
        option_5()
        print()
        break
    
    
