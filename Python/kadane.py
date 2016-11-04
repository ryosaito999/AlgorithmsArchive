inputArr = [-1, -2 , -3 , -4, 1, 2]
print inputArr
maxVal = inputArr[0]

for i in range(0, len(inputArr)):
	tmpval = 0
	if(inputArr[i] < 0):
		continue
	else:
		for j in range(i, len(inputArr)):
			tmpval += inputArr[j]
			if( tmpval > maxVal):
				maxVal = tmpval
			if(tmpval < 0):
				break
print maxVal

