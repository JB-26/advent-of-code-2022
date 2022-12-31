import csv

elves = []
calories = []

with open('day1Input.txt') as csvFile:
	csv_reader = csv.reader(csvFile)
	elf = []
	for row in csv_reader:
		if row == []:
			elves.append(elf)
			elf = []
		else:
			elf.append(f'{", ".join(row)}')

count = 0
for i in elves:
	count+=1

print(f'Complete! There are {count} elves')

for elf in elves:
	caloriesTotal = 0
	for i in elf:
		caloriesTotal = caloriesTotal + int(i)
	calories.append(caloriesTotal)
print('Before')
print(calories)	
calories.sort()
print("Calories list has been sorted!")
print(calories)

		
	