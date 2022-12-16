
print('Advent of Code - Day 1')
print("")

input_file = './day1/input.txt'

inventories: list[list[int]] = []

with open(input_file, newline='') as input:
    inventory: list[int] = []
    for line in input:
        value = line.strip()
        if value == '':
            inventories.append(inventory)
            inventory = []
        else:
            inventory.append(int(value))

inventorySums: list[int] = []
for inventory in inventories:
    sum = 0
    for calories in inventory:
        sum += calories
    inventorySums.append(sum)

elfWithtotal: list[tuple[int, int]] = list(enumerate(inventorySums))

elfWithtotal.sort(reverse=True, key= lambda x: x[1])

top = elfWithtotal[0:3]

topSum = 0
for elf, sum in top:
    topSum += sum
    print(f"Elf {elf + 1} has {sum} calories!")

print(f"Their total is {topSum} calories!")

# rb61 13:56 herfort
# ic 2047 15:38 spoor 4 hannover