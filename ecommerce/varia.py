# from ecommerce.shipping import cal_shipping
from pathlib import Path
S = 'Python'


P = [S[:i]
for i in range(len(S)+1)]

print(*(P+P[::-1]), sep = '\n')



number = 7

while True:
    user_input = input('Would you like to play our guessing game Y/n: ')
    if user_input == 'n':
        break
    user_input = int(input('Guess our special number: '))
    if user_input == number:
        print('You guessed correctly:')
    elif abs(number - user_input) == -1:
        print('You were off by one')
    else:
        print('Sorry!! your guess was wrong')





path = Path('ecommerce')
print(path.exists())
