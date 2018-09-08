import random

output = "../crop_part1/shuffled.txt"

with open("../crop_part1/names.txt") as f:
	content = f.readlines()

# Stripping /n from lines
content = [x.strip() for x in content]

random.shuffle(content)

f = open(output, 'w')
for line in content:
	f.write(line)
	f.write('\n')

f.close()



