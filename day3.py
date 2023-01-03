import csv

totalSum = 0

rucksacks = []
lettersScore = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39,
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52
}

with open('day3Input.txt') as csvFile:
    csv_reader = csv.reader(csvFile)
    line_count = 0
    for row in csv_reader:
        rucksacks.append(f"".join(row))

# part one
for i in rucksacks:
    firstPartMatch = []
    tempListFull = [*i]
    # slicing strings
    tempListFirst = [*i[:int(len(i) / 2)]]
    tempListSecond = [*i[int(len(i) / 2):]]
    is_looping = True
    for i in tempListSecond:
        for x in tempListFirst:
            if i == x:
                totalSum += lettersScore[x]
                is_looping = False
                break
        if not is_looping:
            break

print(totalSum)
totalSum = 0

# part two
elf_rucksack = []
for i in rucksacks:
    unpacked_item = [*i]
    elf_rucksack.append(unpacked_item)
    if len(elf_rucksack) == 3:
        first_item = elf_rucksack[0]
        second_item = elf_rucksack[1]
        third_item = elf_rucksack[2]
        is_looping = True
        for x in first_item:
            for y in second_item:
                if x == y:
                    match_char = x
                    for z in third_item:
                        if z == x:
                            totalSum += lettersScore[x]
                            is_looping = False
                            break
                    break
            if not is_looping:
                elf_rucksack.clear()
                first_item.clear()
                second_item.clear()
                third_item.clear()
                break
print(totalSum)
