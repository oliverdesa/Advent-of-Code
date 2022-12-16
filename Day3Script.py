from string import ascii_letters

with open('Rucksacks.txt') as file:
   data = [i for i in file.read().strip().split('\n')]

x = 0
allGroups = []
group = []
for rucksack in data:
   x += 1
   group.append(set(rucksack))
   if x == 3:
      allGroups.append(group)
      group = []
      x = 0
   
totalSum = 0
for group in allGroups:
   for priority, char in enumerate(ascii_letters):
      if char in group[0] and char in group[1] and char in group[2]:
         totalSum += priority + 1

print(totalSum)




# totalSum = 0
# for rucksack in data:
#    half = len(rucksack)//2
   
#    left = set(rucksack[:half])
#    right = set(rucksack[half:])

#    for priority, char in enumerate(ascii_letters):
#       if char in left and char in right:
#          totalSum += priority + 1







        

        
