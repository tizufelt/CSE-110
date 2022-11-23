# catNames = []
# while True:
#     print('Enter the name of cat ' + str(len(catNames) + 1) +
#        ' (Or enter nothing to stop.):')
#     name = input()
#     if name == '':
#          break
#     catNames = catNames + [name]  # list concatenation
# print('The cat names are:')
# for name in catNames:
#      print('  ' + name)

######################################################
for x in range(0.5, 5.5, 0.5):
  print(x)
    

 res = {val : idx + 1 for idx, val in enumerate(cart)}
 
 
 
 def option_2():
    print()
    print(f" You have {len(cart)} items in your shopping cart")
    print()
    for item in cart:
        print(f"  {item.upper()} - ${cart [item]:.2f}")