import random

my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'peach', 'quince', 'raspberry', 'strawberry', 'tangerine', 'watermelon', 'apricot', 'blueberry', 'cantaloupe', 'dragonfruit', 'jackfruit', 'papaya', 'starfruit', 'coconut', 'pomegranate', 'persimmon', 'cranberry', 'currant', 'gooseberry', 'mulberry', 'boysenberry', 'loganberry', 'salak', 'soursop', 'tamarind', 'ugli fruit', 'yuzu']
k = 5

def check_guess():
    selected = random.choice(my_list)
    selected = list(selected)
    blind = ['*']*len(selected)
    check = selected.copy()
    print('Welcome to the Word Guessing Game!')
    print(f'The word has {len(selected)} letters.')

    for i in range(len(check)+k):
        print('Guess a leter:', end=' ')
        guess = input().lower()
        if guess in check:
            for j in range(len(selected)):
                if selected[j] == guess:
                    if blind[j] == '*':
                        blind[j] = guess
                        check.remove(guess)
                        break
            print(' '.join(blind))
        else:
            print('not matched')
            print(' '.join(blind))
        if blind == selected:
            break


    if blind == selected:
        print(f'=====================================\nthe word: {' '.join(selected)}')
        print('---You win!---\n====================================')
    else:
        print(f'~~~~~~~~~~~~~\nthe word: {' '.join(selected)}, your guess: {' '.join(blind)}')
        print('---You lose!---\n~~~~~~~~~~~~~~~~')

def ask_again():
    print('Do you want to play again? (y/n)')
    answer = input().lower()
    if answer == 'y':
        check_guess()
        ask_again()
    elif answer == 'n':
        print('Thanks for playing!')
    else:
        print('Invalid input. Please enter "y" or "n".')
        ask_again()

check_guess()
ask_again()
