""" 
Tim Zufelt
CSE 110 
L12 Milestone 
"""

import csv



userinput = int(input("Enter in the year of interest: "))

with open("life-expectancy.csv") as data_file:
    next(data_file)
    
    maxlife = -9999
    maxname = ""
    maxyear = ""
    
    minlife = 9999
    minname = ""
    minyear = ""
    
    smaxlife = -9999
    smaxname = ""
    smaxyear = ""
    
    sminlife = 9999
    sminname = ""
    sminyear = ""
    
    for line in data_file:
        data = line.strip()
        parts = data.split(",")
        country = parts[0]
        code = parts[1]
        year = int(parts[2])
        lifeExp = float(parts[3])
        
        if lifeExp > maxlife:
            maxlife = lifeExp
            maxname = country
            maxyear = year
        
        if lifeExp < minlife:
            minlife = lifeExp
            minname = country
            minyear = year
            
        if userinput == year:
            if lifeExp > smaxlife:
                smaxlife = lifeExp
                smaxname = country
            if lifeExp < sminlife:
                sminlife = lifeExp
                sminname = country
            #total = 0
            #for i in range(len(country)):
                #total += lifeExp[i]
                #average = total / len(country)
                
print(f"\nThe overall max life expectancy is: {maxlife:.2f} from {maxname} from {maxyear}. ")
print(f"The overall min life expectancy is: {minlife:.2f} from {minname} in {minyear}. ")
print (f"\nFor the year {userinput}: ")
print (f"The max life expectancy was in : {smaxname} with {smaxlife:.2f}")
print (f"The min life expectancy was in : {sminname} with {sminlife:.2f}")

