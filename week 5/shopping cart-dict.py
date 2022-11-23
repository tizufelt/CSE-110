


cart = {} 
print()
print()
print("#############################################\n"
      "###                                       ###\n"
      "###    Welcome to Your Shopping Cart      ###\n"
      "###                                       ###\n"
      "#############################################")
print()
 
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
    select = int(input("> "))
 
    if select == 1:
        item = input(" What would you like to add?  ")
        price = float(input(" type in the price "))
        cart [item] = price
        print(f"'{item.capitalize()}' has been added to your cart.")
        print(f" The price is ${price}")
 
    if select == 2:
        print("This is what is in your shopping cart")
        for item in cart:
            print(f"  {item} - ${cart [item]}")
 
    if select == 3:
        takeout = input(" Type in what you would like to remove?  ")
        cart.pop(takeout)
 
    if select == 4:
        total = 0
        for item in cart:
            total += cart [item]
        print(f" ${total}")
 
    if select == 5:
        print ("comeback soon.")
        break