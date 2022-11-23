

cart = []
price = []

def welcome_menu():
    print()
    print()
    print("#############################################\n"
          "###                                       ###\n"
          "###    Welcome to Your Shopping Cart      ###\n"
          "###                                       ###\n"
          "#############################################")

welcome_menu()


while True:
    print()
    print ("Please choose from the menu below")
    print()
    print ("1. Add item. ")
    print ("2. View cart. ")
    print ("3. Remove Item. ")
    print ("4 compute total.")
    print ("5. exit cart.")
    print()
    option = int(input("> "))
    
        
    if option == 1:#add item option
        item = input(" What would you like to add?  ")
        price = float(input(" type in the price: "))
        print()
        cart [item] = price
        print(f"'{item.upper()}' has been added to your cart.")
        print(f" The price is ${price:.2f}")
        
    elif option == 2:# view cart option
        if cart:
            print("This is what is in your shopping cart: ")
            print()
            print(f"There are {len(cart)} items in your cart: ")
        for item in cart:
            print(f"  {item.upper()} - ${cart [item]:.2f}")
            
     
            
    elif option == "3": #remove item from cart option
        delete = input("Enter the item you want removed. ")
        cart.remove(delete)
        print(f"the item {delete} has been removed from your list. ")        
   
    elif option == "4":# eventually the price feature
        print("Show total in cart if I knew how")
    
    elif option == "5":# EXIT option
        print("Thank you for shopping with us... Bye. ")
        break
    
    else:
        print("\n There is nothing in your cart, sorry.\n")   
        