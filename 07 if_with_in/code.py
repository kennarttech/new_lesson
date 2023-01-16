number = 7


user_input = input("Enter 'y' if you would like to play:  ").lower()


if user_input == 'y':
    user_number = int(input('Guess our number for price: '))
    if user_number == number:
        print('You guess correctly')
    else:
        print('Sorry, its wrong')
