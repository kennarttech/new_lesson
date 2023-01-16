number = 7



while True:
    user_input = input("Do you want to play N/y:  ").lower()
    if user_input == 'n':
        break
    user_input2 = int(input('Please enter ur magic number'))
    if number == user_input2:
        print('Your guess is correct')
        break
    else:
        print('You guess a wrong number')




playGame = True

while playGame:
    print('We are playing the game')

    playAgain = input('Would you like to playAgain? ')

    if playAgain == 'n' or playAgain == 'no':
        playGame = False

print('Thank you for playing')




usernames = ['Tony', 'asmith', 'Angela']

userChoice = ''

while userChoice not in usernames:
    userChoice = input('Type in your username: ')

print('Hi ' + userChoice)





command = ""
started = False


options = ['(start = start the car)\n(stop = stop the car)' ]

for m in options:
    print(m)


while True:
    command = input('Enter ur option...').lower()
    if command == 'start':
        if started:
            print('Car is already started')
        else:
            started = True
            print('Car started.....')
    elif command == 'stop':
        if not started:
            print('Car already stopped')
        else:
            started = False
            print('Car stopped.')
        break
    else:
        print("Sorry i don't understand the option")
        print(options)
# =========End of while loop==========
