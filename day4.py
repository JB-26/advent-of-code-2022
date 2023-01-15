#TODO: Use 'range' to count between numbers
#TODO: Maybe use regex to find the numbers?
import csv
import re

list = []
pairs = []
totalList = []

with open('day4Input.txt') as csvFile:
    csv_reader = csv.reader(csvFile, delimiter=' ')
    line_count = 0
    for row in csv_reader:
        list.append(f"".join(row))
for item in list:
    rangeList1 = []
    rangeList2 = []
    list1 = []
    list2 = []
    counter = 0
    print(item)
    temp = [*item]
    test = re.split(r',|-', item)
    print(test)
    for i in test:
        print(i)
        if counter < 2:
            list1.append(i)
            counter += 1
        else:
            list2.append(i)
    for value in range(int(list1[0]), int(list1[1]), 1):
        print(value)
        rangeList1.append(value)
    for value in range(int(list2[0]), int(list2[1]), 1):
        print(value)
        rangeList2.append(value)
    totalList.append(rangeList1)
    totalList.append(rangeList2)
    #for i in temp:
        #try:
            #if int(i):
                #print(i)
            #elif i == '-':
                #print('SPECIAL CHARACTER DETECTED')
                #pass
        #except:
            #pass
