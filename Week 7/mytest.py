import math



def CToF(celsius):
    return((9.0/5.0)*celsius+32)

def windchill(temp, wind):
    formula = 13.12+0.6215*temp- 11.37*math.pow(wind, 0.16) + \
          0.3965*temp*math.pow(wind, 0.16)
    return formula


def main():
    temp = float(input("what is the temperature? "))
    choice = input("Fahrenheit or Celsuis? (F or C: ")
    if choice == "F" or choice == "f":
        for i in range(5, 65, 5):
            wc = windchill(temp, i)
            print("At temperature %.1fF, and wind speed %d mph, the windchill is: %.2fF" % (temp, i, wc))
    elif choice =="C" or choice =="c":
        temp = CToF(temp)
        for i in range(5, 65 ,5):
            wc = windchill(temp, i)
            print("At temperature %.1fF, and wind speed %d mph, the windchill is: %.2fF" % (temp, i, wc))
            

main()    








