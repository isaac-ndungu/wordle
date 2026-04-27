import random
from .utils import get_word_list, give_feedback, check_guess, initialize_keyboard, update_keyboard, display_keyboard, show_welcome
from .stats import update_stats, display_stats

def choose_difficulty():
    print('\nChoose difficulty:')
    print('1. Easy   (8 chances)')
    print('2. Normal (6 chances)')
    print('3. Hard   (4 chances)')

    difficulty = {'1': 8, '2': 6, '3': 4}

    while True:
        choice = input('Enter 1, 2 or 3: ').strip()
        if choice in difficulty:
            return difficulty[choice]
        print('Invalid choice. Please enter 1, 2 or 3.')

def run_game():
    show_welcome()
    word_list = get_word_list()

    while True:
        user_input = input('Play a game? (y/n): ').strip().lower()

        if user_input == 'n':
            display_stats()
            print('Bye!')
            break

        elif user_input == 'y':
            secret_word = random.choice(word_list)
            print(secret_word)

            keyboard = initialize_keyboard()
            difficulty = choose_difficulty()
            chances = 1

            while chances <= difficulty:
                player_input = input('Enter your Guess: ').strip().upper()
                result = check_guess(player_input, secret_word, chances, word_list)

                if result == 'win':
                    update_stats(won=True, chances=chances, difficulty=difficulty)
                    display_stats()
                    break
                elif result == 'invalid':
                    continue

                keyboard = update_keyboard(keyboard, player_input, secret_word)
                display_keyboard(keyboard)
                chances += 1
            else:
                print(f'Oops! The word was {secret_word}')
                update_stats(won=False, chances=chances, difficulty=difficulty)
                display_stats()
        else:
            print('Invalid input')
            continue