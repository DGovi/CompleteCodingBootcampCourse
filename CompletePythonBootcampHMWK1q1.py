# *******************First question********************************** 
# write a function that computes the volume of a sphere given its radius

import math

def vol(rad):
	return math.pi * rad ** 2; 

#test
#print(vol(2));

#*******************************Second Question ***************************
# write a function that checks whether a number is in a givin range ( inclusive of high and low)

def inRange(num, high, low):
	return low <=  num <= high;

#test
#print(inRange(1,2,3))

#******************************Third  Question ***************************
#write a function thhat accepts a string and calculates the number of upper case and lower case

def numUpperAndLower(aString):
	numUpper = 0;
	numLower = 0;

	for letter in aString:
		if letter.isupper():
			numUpper += 1;
		else:
			numLower += 1;
	print("there are " + str(numUpper) + " upper case and " + str(numLower) + " lower case")

#test
#numUpperAndLower("DAniel")

