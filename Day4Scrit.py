# Advent of Code Day 4

with open('Day4Puzzle.txt') as file:
    data = file.readlines()

data = [pair.strip().split(',') for pair in data]

for pair in data:
    for index, spread in enumerate(pair):
        lower, upper = spread.split('-')
        pair[index] = lower, upper


count = 0
# for pair in data:
#     if (int(pair[0][0]) >= int(pair[1][0])) or (int(pair[0][1]) <= int(pair[1][1])):
#         count += 1
#     elif (int(pair[1][0]) >= int(pair[0][0])) or (int(pair[1][1]) <= int(pair[0][1])):
#         count += 1

# print(count)


# Part 2

#print(data)

for pair in data:
    range1 = list(range(int(pair[0][0]), int(pair[0][1])+1))
    range2 = list(range(int(pair[1][0]), int(pair[1][1])+1))
    if len(set(range1).intersection(range2)) > 0:
        count += 1


print(count)
    
