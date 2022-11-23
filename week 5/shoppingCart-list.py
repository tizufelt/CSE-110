




cart = []
itemprice = []


while True:
    if cart:
        pass
    else:
        print("\nYour shopping cart is empty. \n")
    print("Shopping Cart Options\n")
    print("1. Add item")
    print('2. Remove item')
    print("3. View Total")
    print("4. Exit Cart")
    
    option = input("> ")
    
    if option == "1":
        pass
        item = input(" What would you like to add?  ")
        cart.append(item)
        print(f"'{item}' has been added to your cart.")
       
        
    if option =="2":
        pass
        print("This is what is in your shopping cart")
        for item in cart:
            print(item)
            break
    else:
        print("\nThere are no items in your cart. \n")
        
    if option =="3":
        total = 0
        for item in cart:
            total += cart [item]
        print(f"${total}")
    if option =="3":
        pass
    else:
        print("\nYour cart is empty.\n")
        check = "yes"
    if check =="yes":
        print("\n Cart Closed")
        break
        
        