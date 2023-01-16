import math


def atm_cash(original_pin, balance):
    """This function compute and the return the balance if fun is available"""
    pin = int(input('Enter your pin: '))
    if pin == original_pin:
        amount = int(input('Enter withdraw amount: '))
        if amount <= balance:
            bal = balance -amount 
            print(f'Withdrawl Successful your balance is {bal}')
        else:
            print('Balance not Available')
    else:
        print('Please Enter a Correct PIN!')


RESULT = atm_cash(1234, 1009721750)
print(RESULT)