



people = ["Stephanie 36", 
          "John 29",
          "Emily 24",
          "Gretchen 54",
          "Noah 12",
          "Penelope 32",
          "Michael 2",
          "Jacob 10"
          ]

youngage = 9999
youngname = ""

for personLine in people:
    parts = personLine.split()
    name = parts[0]
    age = int(parts[1])
    
    if age < youngage:
        youngage = age
        youngname = name
        
print(f"THe youngest person is: {youngname} with age as {youngage} ")

        