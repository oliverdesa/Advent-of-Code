# Advent of code day 3 script

file = open('Rucksacks.txt', 'r')
Rsacks = file.readlines()
file.close()

Rsacks = [content.strip() for content in Rsacks]

comp1 = []
for sack in Rsacks:
   comp2 = [sack[item] for item in range(int(len(sack)/2))]
   comp1.append(comp2)

#for sack in Rsacks:
   #for item in range(int(len(sack)/2), len(sack)):
      
hits = []
for index, sack in enumerate(Rsacks):
   for item in enumerate(sack, start = int(len(sack)/2)):
      presence = comp1[index].count(item[1])
      





        

        
