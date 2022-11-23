numblist = []
number = -1


while number != 0:
    number = int(input("Enter your number: "))
    
    if number != 0:
        numblist.append(number)

sum = 0
for number in numblist:
    sum += number
print(f"the sum is : {sum}")

count = len(numblist)
average = sum/count

print(f" THe average is: {average}")
   
bestnumber = -1
 
for number in numblist:
    if number > bestnumber:
        bestnumber = number

print(f" The largest number is: {bestnumber}")


smallnumb = 999999999999

for number in numblist:
    if number > 0 and number < smallnumb:
        smallnumb = number

print(f"the smallest positive number is: {smallnumb}")

sort = sorted(numblist)

print(" the sorted list is:")
for number in sort:
    print(number)



    