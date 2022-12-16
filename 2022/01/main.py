
print('Advent of Code - Day 1')
print("")

input_file: str = './2022/01/input.txt'
top_n: int = 3

inventories: list[list[int]] = []
with open(input_file) as input:
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

topSum = 0
for elf, sum in elfWithtotal[0:top_n]:
    topSum += sum
    print(f"Elf {elf + 1} has {sum} calories")

print(f"Together they have {topSum} calories!")
