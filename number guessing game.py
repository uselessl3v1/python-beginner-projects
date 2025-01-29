secret_number = 9
guess = 0
tries = 0
max_tries = 3
def number_guessing_game(secret_number=9, max_tries=3, guess=0, tries=0):
    print('''
    
    ''' * 100)
    while tries < max_tries and int(guess) != secret_number:
        try:
            guess = input("Guess: ")
            tries += 1
            if int(guess) == secret_number:
                print('You win!')
                break
            elif tries >= max_tries and int(guess) != secret_number:
                print('You lose!')
        except ValueError:
            print('Please try again and enter a valid value.')
            break
selected_secret_number = input("What do you want the secret number to be? ")
selected_tries = input("How many tries do you want? ")
number_guessing_game(int(selected_secret_number), int(selected_tries))
