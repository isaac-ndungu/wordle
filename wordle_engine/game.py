import random
from .utils import get_word_list, give_feedback, check_guess, initialize_keyboard, update_keyboard, display_keyboard

def run_game():
    word_list = get_word_list()
    secret_word = random.choice(word_list)
    keyboard = initialize_keyboard()

    print('----- Wordle-----')
    print('Guess your way to the correct word')

    while True: 
        user_input = input('Get 6 chances to guess a word. Play? (y/n):').strip().lower()
        
        if user_input == 'n':
            print('Bye')
            break
            
        elif user_input == 'y':
            chances = 1
            while chances <= 6:
                player_input = input('Enter your Guess:').strip().upper()
                result = check_guess(player_input, secret_word, chances, word_list)
                if result == 'win':
                    break
                elif result == 'invalid':
                    continue
                
                keyboard = update_keyboard(keyboard, player_input, secret_word)
                display_keyboard(keyboard)
                chances += 1
            else:
                print('Oops, you ran out of guesses!')
        else:
            print('Invalid input')
            continue