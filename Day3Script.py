from string import ascii_letters

with open('Rucksacks.txt') as file:
   data = [i for i in file.read().strip().split('\n')]


totalSum = 0
for rucksack in data:
   half = len(rucksack)//2
   
   left = set(rucksack[:half])
   right = set(rucksack[half:])

   for priority, char in enumerate(ascii_letters):
      if char in left and char in right:
         totalSum += priority + 1

print(totalSum)





        

        
