

import csv

count = 0
lowest = 500
lowestYear = ''
lowestCountry = ''

highest = 0
highestYear = ''
highestCountry = ''




with open("life-expectancy.csv") as lifefile:
    for row in lifefile:
        count = count +1
        cleanrow = row.strip()
        words = cleanrow.split(',')
        if count > 1:
            country = words[0]
            code = words[1]
            year = int(words[2])
            life = float(words[3])
                      
            if life < lowest:
                lowest = life
                lowestYear = year
                lowestCountry = country

                if life > highest:
                    highest = life
                    highestYear = year
                    highestCountry = country

                
           
                
print()                
print(f"The lowest life expectancy is: {lowest} in {lowestCountry} in the year {lowestYear}. ")
print()
print(f"The highest life expectancy is: {highest} in {highestCountry} in the year {highestYear}. ")
print()



    
    
           
            
            
            
#average = average / numChoiceYears            
#print(f" Lowest: {lowest:.2f} - {lowestYear} - {lowestCountry}")         
        

            