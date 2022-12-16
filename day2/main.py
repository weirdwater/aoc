from enum import Enum

print('Advent of Code - Day 2')
print("")

input_file: str = './day2/input.txt'

# Score:
#   + 1 for choosing Rock a/x
#   + 2 for choosing Paper b/y
#   + 3 for choosing Scissors c/z
#   + 0 for loss
#   + 3 for draw
#   + 6 for win

class Result(Enum):
    Win = 6
    Draw = 3
    Lose = 0

label_for_choice = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
}

score_for_choice = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

results_for_choice = {
    'X': {
        'A': Result.Draw,
        'B': Result.Lose,
        'C': Result.Win
    },
    'Y': {
        'A': Result.Win,
        'B': Result.Draw,
        'C': Result.Lose
    },
    'Z': {
        'A': Result.Lose,
        'B': Result.Win,
        'C': Result.Draw
    }
}


def calc_score(choice_player: str, choice_other: str) -> int:
    base_score = score_for_choice.get(choice_player, 0)
    result = results_for_choice.get(choice_player, {}).get(choice_other, Result.Lose)
    return base_score + result.value

score = 0
with open(input_file) as file:
    for line in file:
        other, player = line.strip().split(" ")
        result = calc_score(player, other)
        print(f"The other chooses {label_for_choice.get(other, 'unknown')}, respond with {label_for_choice.get(player, 'unkown')}: {result}")
        score += result

print(f"Total score: {score}")
