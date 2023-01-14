import csv

list = []
pairs = []

with open('day4Input.txt') as csvFile:
    csv_reader = csv.reader(csvFile, delimiter=' ')
    line_count = 0
    for row in csv_reader:
        list.append(f"".join(row))
for item in list:
    print(item)
    temp = [*item]
    for i in temp:
        try:
            if int(i):
                print(i)
            elif i == '-':
                print('SPECIAL CHARACTER DETECTED')
                pass
        except:
            pass
