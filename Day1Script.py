# Advent of Code Day 1

# Proof of account ownership ownerproof-2622103-1670101117-495058b07a1c

calories = open('input.txt', 'r')
calorieList = calories.readlines()

summedCals = []
calCounter = 0
for cal in range(len(calorieList)):
    if calorieList[cal] != '\n':
        calCounter += int(calorieList[cal].strip('\n'))
    else:
        summedCals.append(calCounter)
        calCounter = 0

# targetElf = max(summedCals)
# print(targetElf)

summedCals.sort(reverse=True)

topThree = sum(summedCals[0:3])

print(topThree)

calories.close()