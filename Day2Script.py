# Advent of Code Day 2
import numpy as py
import pandas as pd


x = np.array([dawdwd])
print(x)

puzzle = open('Day2Puzzle.txt', 'r')

matches = puzzle.readlines()
for match in range(len(matches)):
    matches[match] = matches[match].strip('\n').split()

puzzle.close()

# Part 1

def matchCalculator(opponent, mine):
    if opponent == 'A':
        if mine == 'X':
            score = 1 + 3
        elif mine == 'Y':
            score = 2 + 6
        else:
            score = 3 + 0
    if opponent == 'B':
        if mine == 'X':
            score = 1 + 0
        elif mine == 'Y':
            score = 2 + 3
        else:
            score = 3 + 6
    if opponent == 'C':
        if mine == 'X':
            score = 1 + 6
        elif mine == 'Y':
            score = 2 + 0
        else:
            score = 3 + 3
    return score

totalScore = 0
for match in range(len(matches)):
    score = matchCalculator(matches[match][0], matches[match][1])
    totalScore += score

print(totalScore)
