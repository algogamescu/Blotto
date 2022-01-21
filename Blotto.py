import itertools
import csv
import math
def battle(list1,list2):
    result = [0,0]
    for i in range(10):
        if list1[i] > list2[i]:
            result[0] += i+1
        elif list1[i] == list2[i]:
            result[0] += (i+1)/2
            result[1] += (i+1)/2
        else:
            result[1] += i+1
    return result

people = {}
with open('people.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        entry = [int(x) for x in row[1:11]]
        scaled_entry = [math.floor(1000*x/sum(entry)) for x in entry]
        people[row[12]] = [row[11],scaled_entry,0]

print(people)
pairsOfPeople = itertools.combinations(people,2)

for pair in pairsOfPeople:
    deltas = battle(people[pair[0]][1],people[pair[1]][1])
    people[pair[0]][2] += deltas[0]
    people[pair[1]][2] += deltas[1]

sorted_people = sorted(people.items(), key=lambda item: item[1][2], reverse=True)

print(sorted_people)