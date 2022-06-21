'''
CS3A, Assignment #3, Mortgage Calculator
Brandon Cunnane
'''

import sys

MIN_PRINCIPAL = 100000
MAX_PRINCIPAL = 1000000
MIN_CREDIT_SCORE = 300
MAX_CREDIT_SCORE = 850
GOOD_CREDIT_SCORE_THRESHOLD = 650

principal = int(input(f'Please enter mortgage amount '
                        f'({MIN_PRINCIPAL} - {MAX_PRINCIPAL}): '))
if not(MIN_PRINCIPAL <= principal <= MAX_PRINCIPAL):
    print(f'Mortgage amount must be between '
          f'{MIN_PRINCIPAL} and {MAX_PRINCIPAL}')
    sys.exit(1)

num_yrs = int(input('Please enter mortgage period in years (10, 15, 30): '))
if not(num_yrs == 10 or num_yrs == 15 or num_yrs == 30):
    print('Mortgage period must be 10, 15, or 30 years')
    sys.exit(1)

credit_score = int(input(f'Please enter your credit score '
                         f'({MIN_CREDIT_SCORE} - {MAX_CREDIT_SCORE}): '))
if not(MIN_CREDIT_SCORE <= credit_score <= MAX_CREDIT_SCORE):
    print(f'Credit score must be between '
          f'{MIN_CREDIT_SCORE} and {MAX_CREDIT_SCORE}')
    sys.exit(1)

if credit_score > GOOD_CREDIT_SCORE_THRESHOLD:
    if num_yrs == 10:
        yr_rate = 0.03
    elif num_yrs == 15:
        yr_rate = 0.035
    else:
        yr_rate = 0.04
else:
    if num_yrs == 10:
        yr_rate = 0.0325
    elif num_yrs == 15:
        yr_rate = 0.0375
    else:
        yr_rate = 0.045

mo_rate = yr_rate / 12
num_months = num_yrs * 12
mo_payment = (principal * (mo_rate * (1 + mo_rate) ** num_months)
              / (((1+mo_rate)**num_months)-1))

print(f'Your annual interest rate is {yr_rate:0.2%}')
print(f'Your monthly payment is ${mo_payment:06.2f}')
