import random
from colorama import Fore, Back, Style

def get_word_list():
    word_list = []
    with open('words.txt', 'r', encoding='utf-8') as file:
        words = [line.strip('\n') for line in file]
        for word in words: 
            word_list.append(word.upper())
    return word_list

def give_feedback(player_input, secret_word):
    output = ''
    for index, letter in enumerate(player_input):
        if letter not in secret_word:
            output += Fore.WHITE + letter
        elif letter == secret_word[index]:
            output += Fore.GREEN + letter
        else: 
            output += Fore.YELLOW + letter

    print(output + Style.RESET_ALL)

def check_guess(player_input, secret_word, chances, word_list):
    if (len(player_input) != 5) or (player_input not in word_list):
        print('Not a valid word. Try again')
        return 'invalid'
    elif player_input == secret_word:
        output = Fore.GREEN + player_input
        print(output + Style.RESET_ALL)

        print(f'You got it in {chances} guesses')
        return 'win'
    else:
        give_feedback(player_input, secret_word)
        return 'continue'

def initialize_keyboard():
    return {letter: 'unused' for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}

def update_keyboard(keyboard, player_input, secret_word): 
    for index, letter in enumerate(player_input):
        if letter == secret_word[index]:
            keyboard[letter] = 'correct'
        elif letter in secret_word:
            # only downgrade if not already green
            if keyboard[letter] != 'correct':
                keyboard[letter] = 'present'
        else:
            keyboard[letter] = 'absent'
    return keyboard

def display_keyboard(keyboard):
    color_map = {
        'unused': Fore.WHITE,
        'correct': Fore.GREEN,
        'present': Fore.YELLOW,
        'absent': Fore.BLACK
    }
    print('\n')
    for letter, state in keyboard.items():
        print(color_map[state] + letter + Style.RESET_ALL, end=' ')
    print('\n')