


mylist = []
item = None

while item != "quit":
    item = input("item: ")
    
    if item != "quit":
        mylist.append(item)
        
print("\nThe shopping list is: ")
for item in mylist:
    print(item)

print("\n The shopping list with indexes is: ") 
for i in range (len(mylist)):
    item = mylist[i]
    print(f"{i}. {item}")
    
print()
index = int(input(" Which item would you like to change? "))
for x in range(len(mylist)):
    item = mylist[x]
    print(f"{x}. {item}")


        
    