# for reference
# first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors.
# second column is what you play in response: X for Rock, Y for Paper, and Z for Scissors.
# The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

import csv

round = 0
numOfRounds = 0
playerScore = 0

with open('day2Input.txt') as csvFile:
	csv_reader = csv.reader(csvFile, delimiter=' ')
	line_count = 0
	opponentColumn = []
	playerColumn = []
	for row in csv_reader:
		opponentColumn.append(f'{row[0]}')
		playerColumn.append(f'{row[1]}')
		
for i in opponentColumn:
	numOfRounds += 1

while round < numOfRounds:
	print("Playing Rock, Paper, Scissors!")
	print(f"Round - {round}")
	print(f"Opponent picked - {opponentColumn[round]}")
	print(f"You picked - {playerColumn[round]}")

	if opponentColumn[round] == 'A' and playerColumn[round] == 'X':
		print('TIE')
		# shape
		playerScore += 1
		# match result
		playerScore += 3
	
	if opponentColumn[round] == 'A' and playerColumn[round] == 'Y':
		print('WIN')
		# shape
		playerScore += 2
		# match result
		playerScore += 6
	
	if opponentColumn[round] == 'A' and playerColumn[round] == 'Z':
		print('LOSE')
		# shape
		playerScore += 3
		# match result
		playerScore += 0
	
	if opponentColumn[round] == 'B' and playerColumn[round] == 'X':
		print('LOSE')
		# shape
		playerScore += 1
		# match result
		playerScore += 0
	
	if opponentColumn[round] == 'B' and playerColumn[round] == 'Y':
		print('TIE')
		# shape
		playerScore += 2
		# match result
		playerScore += 3
	
	if opponentColumn[round] == 'B' and playerColumn[round] == 'Z':
		print('WIN')
		# shape
		playerScore += 3
		# match result
		playerScore += 6
		
	if opponentColumn[round] == 'C' and playerColumn[round] == 'X':
		print('WIN')
		# shape
		playerScore += 1
		# match result
		playerScore += 6
	
	if opponentColumn[round] == 'C' and playerColumn[round] == 'Y':
		print('LOSE')
		# shape
		playerScore += 2
		# match result
		playerScore += 0
	
	if opponentColumn[round] == 'C' and playerColumn[round] == 'Z':
		print('TIE')
		# shape
		playerScore += 3
		# match result
		playerScore += 3
	
	round += 1
	
print('Finish!')

print(f'Total score is {playerScore}')


# PART TWO
# first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors.
# the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
# The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated
# The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

# reset
playerScore = 0
round = 0

while round < numOfRounds:
	print("Playing Rock, Paper, Scissors!")
	print(f"Round - {round}")
	print(f"Opponent picked - {opponentColumn[round]}")
	print(f"You picked - {playerColumn[round]}")

	if opponentColumn[round] == 'A' and playerColumn[round] == 'X':
		print('LOSE')
		# shape
		playerScore += 3
		# match result
		playerScore += 0

	if opponentColumn[round] == 'A' and playerColumn[round] == 'Y':
		print('TIE')
		# shape
		playerScore += 1
		# match result
		playerScore += 3

	if opponentColumn[round] == 'A' and playerColumn[round] == 'Z':
		print('WIN')
		# shape
		playerScore += 2
		# match result
		playerScore += 6

	if opponentColumn[round] == 'B' and playerColumn[round] == 'X':
		print('LOSE')
		# shape
		playerScore += 1
		# match result
		playerScore += 0

	if opponentColumn[round] == 'B' and playerColumn[round] == 'Y':
		print('TIE')
		# shape
		playerScore += 2
		# match result
		playerScore += 3

	if opponentColumn[round] == 'B' and playerColumn[round] == 'Z':
		print('WIN')
		# shape
		playerScore += 3
		# match result
		playerScore += 6
	
	if opponentColumn[round] == 'C' and playerColumn[round] == 'X':
		print('LOSE')
		# shape
		playerScore += 2
		# match result
		playerScore += 0

	if opponentColumn[round] == 'C' and playerColumn[round] == 'Y':
		print('TIE')
		# shape
		playerScore += 3
		# match result
		playerScore += 3

	if opponentColumn[round] == 'C' and playerColumn[round] == 'Z':
		print('WIN')
		# shape
		playerScore += 1
		# match result
		playerScore += 6

	round += 1

print('Finish!')

print(f'Total score is {playerScore} PART TWO')