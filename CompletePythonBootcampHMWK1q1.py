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

#*********************************Fourth Question ****************************
#wirte a function that takes a list and returns a new list with uniqque elements of the first list

def uniqueList(arrayOfNumbers):
	uniqueArray = [];
	for currentNum in arrayOfNumbers:
		if(currentNum in uniqueArray):
			continue
		uniqueArray.append(currentNum)
	print(uniqueArray)

#test
#uniqueList([1,1,1,1,2,2,2,3,3,3]);	


#***************Fifth quesiton ************************************************
#write a function to muliply all the numbers in a list

def multiplyElementsInList(arrayOfNumbers):
	result = 1;

	for num in arrayOfNumbers:
		result *=num

	print(result);

#test
#multiplyElementsInList([1,2,3,-4])

#*************************** q6 *******************************************
#write a function that check sif a string is a palindrome

def palindrome(possiblePalindrome):
	x = 0

	wordToAnalyse = possiblePalindrome.replace(" ", "")
	reversedWord = wordToAnalyse[::-1]

	for letter in wordToAnalyse:
		if letter != reversedWord[x]:
			print("not a palindrome")
			return False
		x += 1
	print("is a palindrome")
	return True
#test	 
palindrome("hannah")



