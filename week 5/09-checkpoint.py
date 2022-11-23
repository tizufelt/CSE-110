





friends = []
print()
while True:
    print("please list out each friend " + str(len(friends)+1) +"(or enter END to stop.):")
    print()

    name = input()

    if name == "end":
        break
    print()
    friends = friends + [name]
print("All your friends are...")
for name in friends:
    print(" " + name)


