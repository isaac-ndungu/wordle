import json
from pathlib import Path

STATS_FILE = Path(__file__).parent / 'stats.json'

SCORES = {1: 100, 2: 85, 3: 70, 4: 55, 5: 40, 6: 25}

DIFFICULTY_MULTIPLIER = {8: 1, 6: 1.5, 4: 2}

def load_stats():
    if not STATS_FILE.exists():
        return {
            'total_games': 0,
            'total_wins': 0,
            'current_streak': 0,
            'best_streak': 0,
            'total_score': 0,
            'guess_distribution': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}
        }
    
    with open(STATS_FILE, 'r') as file:
        return json.load(file)


def save_stats(stats):
    with open(STATS_FILE, 'w') as file:
        json.dump(stats, file, indent=4)

def calculate_score(chances, difficulty):
    base_score = SCORES.get(chances, 25)
    multiplier = DIFFICULTY_MULTIPLIER.get(difficulty, 1)

    return int(base_score * multiplier)

def update_stats(won, chances, difficulty):
    stats = load_stats()
    stats['total_games'] += 1

    if won:
        score = calculate_score(chances, difficulty)

        stats['total_wins'] += 1
        stats['current_streak'] += 1
        stats['total_score'] += score
    
        stats['best_streak'] = max(stats['best_streak'], stats['current_streak'])

        if str(chances) in stats['guess_distribution']:
            stats['guess_distribution'][str(chances)] += 1
    else:
        stats['current_streak'] = 0

    save_stats(stats)

def display_stats():
    stats = load_stats()
    total_games = stats['total_games']
    win_rate = (stats['total_wins'] / total_games * 100) if total_games > 0 else 0

    print('\n---------- Statistics ----------')
    print(f"Total Games     : {total_games}")
    print(f"Total Wins      : {stats['total_wins']}")
    print(f"Win Rate        : {win_rate:.1f}%")
    print(f"Current Streak  : {stats['current_streak']}")
    print(f"Best Streak     : {stats['best_streak']}")
    print(f"Total Score     : {stats['total_score']}")
    print('\nGuess Distribution:')
    for guess, count in stats['guess_distribution'].items():
        bar = '-' * count
        print(f"  {guess} | {bar} {count}")
    print('--------------------------------\n')