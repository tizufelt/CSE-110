import statistics
highest_value = -1
min_value = 10000
best_life = -1
min_life = 10000
best_Country = ""
min_Country = ""
max_entity = ""
min_entity = ""
max_year = ""
min_year = ""
counter = 0
total_age = 0
year_interest = input("Enter the year of interest: ")
country_interest = input("Enter the country of interest: ")

with open("life-expectancy.csv") as data_life:
    next(data_life, None)
    for line in data_life:
        parts = line.split(",")
        entity = parts[0]
        code = parts[1]
        year = parts[2]
        expectancy = float(parts[3])
        if expectancy > highest_value:
            highest_value = expectancy
            max_entity = entity
            max_year = year
            if expectancy < min_value:
                min_value = expectancy
                min_entity = entity
                min_year = year
                if year == year_interest:
                    total_age += expectancy
                    counter += 1
                    average = total_age / counter
                    if expectancy > highest_value:
                        highest_value = expectancy
