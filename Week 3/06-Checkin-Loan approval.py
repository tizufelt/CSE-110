"""
TIM ZUFELT
CSE - 110 
Python FLow Control (if-else)
L06-loan calculator
"""

print("For each of these questions, please provide a 1 thru 10 rating:  ")

loan_amount = int(input("How large is the loan? "))
credit = int(input("How good is your credit"))
income = int(input("How high is your income? "))
down_payment = int(input("How large is your down payment? "))


should_loan = False
if loan_amount >= 5:
    if loan_amount >= 7 and income >= 7:
        should_loan = True
    elif credit >=7 or income >= 7:
        if down_payment >= 5:
            should_loan = True
        else:
            should_loan = False
    else:
        should_loan = False
else:
    if credit < 4:
        should_loan = False
    else:
        if income >= 7 or down_payment >= 7:
            should_loan = True
        elif income >= 4 and down_payment >= 4:
            should_loan = True
        else:
            should_loan = False
            
if should_loan:
    print("The answer is yes. This is a good loan. ")
else:
    print("The answer is no. You should not loan this money. ")
    

