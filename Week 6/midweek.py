import csv



count = 0
lowest = 500
lowestYear = ''
lowestCountry = ''
highest = 0
highestYear = ''
highestCountry = ''
#year = input("enter in the year: ")   
with open("life-expectancy.csv") as lifefile:
    for line in lifefile:
       count = count + 1
       cleanline = line.strip()
       words = cleanline.split(',')
       if count > 1:
        if lowest > float(words[3]):
            lowest = float(words[3])
            #print(lowest)
            lowestYear = words[2]
            lowestCountry = words[0]
            print(f'{lowest:.2f} - {lowestYear} - {lowestCountry} ')
        #if highest < float(words[3]):
            #highest = float(words[3])
            #print(highest)
            #highestYear = words[2]
            #highestCountry = words[0]
            #print(f'{highest} - {highestYear} - {highestCountry}')    
      
            