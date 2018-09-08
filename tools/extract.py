from scipy import ndimage

# Extracting the colour matrices and ages from file number num
# 
# Inputs: num = number of file
#         names = the list of file names in shuffled.txt as array
# 
# Outputs:

def extract_jpg(num, names):

	file_name = names[num]

	# Deterining the age (parsing until first '_')
	age = 0
	if file_name[1] == '_':
		age = int(file_name[:1])
	if file_name[2] == '_':
		age = int(file_name[:2])
	if file_name[2] == '_':
		age = int(file_name[:2])

	# Getting colour matrices from jpeg
	img = ndimage.imread('../crop_part1/' + file_name)
	return (age, img)

# Testing

with open("../crop_part1/names.txt") as f:
	content = f.readlines()

# Stripping /n from lines
content = [x.strip() for x in content]

(age, img) = extract_jpg(5, content)
print(age)
print(img.shape)