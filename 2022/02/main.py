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

class Weapon(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

str_to_Weapon = {
    'A': Weapon.Rock,
    'B': Weapon.Paper,
    'C': Weapon.Scissors
}
str_to_Result = {
    'X': Result.Lose,
    'Y': Result.Draw,
    'Z': Result.Win
}

weapon_for_desired_result = {
    Result.Lose: {
        Weapon.Rock: Weapon.Scissors,
        Weapon.Paper: Weapon.Rock,
        Weapon.Scissors: Weapon.Paper
    },
    Result.Draw: {
        Weapon.Rock: Weapon.Rock,
        Weapon.Paper: Weapon.Paper,
        Weapon.Scissors: Weapon.Scissors
    },
    Result.Win: {
        Weapon.Rock: Weapon.Paper,
        Weapon.Paper: Weapon.Scissors,
        Weapon.Scissors: Weapon.Rock
    }
}


def calc_score(desired_result: Result, choice_other: Weapon) -> int:
    choice = weapon_for_desired_result[desired_result][choice_other]
    result = desired_result.value + choice.value
    print(f"The other chooses {choice_other}. We want to {desired_result}, respond with {choice}: {result}")
    return result


score = 0
with open(input_file) as file:
    for line in file:
        other, player = line.strip().split(" ")
        choice_other: Weapon | None = str_to_Weapon.get(other)
        desired_result: Result | None  = str_to_Result.get(player)

        if (choice_other is not None and desired_result is not None):
            result = calc_score(desired_result, choice_other)
            score += result

print("")
print(f"Total score: {score}")
