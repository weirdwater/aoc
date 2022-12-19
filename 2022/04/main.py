import csv

print('Advent of Code - Day 4')
print("")

input_file: str = './2022/04/input.txt'

def has_overlap(left: tuple[int,int], right: tuple[int,int]) -> bool:
    return (left[0] <= right[0] and right[0] <= left[1]) 
    
def has_complete_overlap(left: tuple[int,int], right: tuple[int,int]) -> bool:
    return left[0] <= right[0] and right[1] <= left[1]

def parse_range(str_range: str) -> tuple[int, int]:
    raw = str_range.split('-')
    left, right = map(lambda n: int(n), raw)
    return (left, right)

n_with_overlap = 0
n_with_complete_overlap = 0
with open(input_file) as file:
    reader = csv.reader(file)
    for left_raw, right_raw in reader:
        left = parse_range(left_raw)
        right =  parse_range(right_raw)
        if (has_complete_overlap(left, right) or has_complete_overlap(right, left)):
            n_with_complete_overlap += 1
        if (has_overlap(left, right) or has_overlap(right, left)):
            n_with_overlap += 1

print(f"{n_with_overlap} pairs of elves have overlapping assignments")
print(f"{n_with_complete_overlap} pairs of elves have completely overlapping assignments")
