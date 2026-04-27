import random
from wordle_engine import get_word_list, check_guess

word_list = get_word_list()
secret_word = random.choice(word_list)
# print(secret_word)

chances = 1

while chances <= 6:
    player_input = input('Enter your Guess:').strip().upper()
    result = check_guess(player_input, secret_word, chances)
    if result == 'win':
        break
    elif result == 'invalid':
        continue

    chances += 1
else:
    print('Oops, you ran out of guesses!')