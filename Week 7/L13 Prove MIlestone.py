import math



def CToF(celsius):
    return((9.0/5.0)*celsius+32)

def windchill(temp, wind):
    formula = 35.74+(0.6125*temp)-(35.75*pow(wind,0.16))+(0.4275*temp*pow(wind,0.16))
    return formula


def main():
    temp = float(input("what is the temperature? "))
    choice = input("Fahrenheit or Celsuis? (F or C: ")
    if choice == "F" or choice == "f":
        for i in range(5, 65, 5):
            wc = windchill(temp, i)
            print(f"At temperature {temp:.2f}F, and wind speed {i} mph, the windchill is: {wc:.2f}F")
    elif choice =="C" or choice =="c":
        temp = CToF(temp)
        for i in range(5, 65 ,5):
            wc = windchill(temp, i)
            print(f"At temperature {temp:.2f}F, and wind speed {i} mph, the windchill is: {wc:.2f}F")
            

main()    








