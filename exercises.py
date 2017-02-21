# # # Given a string, print the string uppercased. #string #easy

# # def toUpperCase(stringToChangeToUpperCase):
# # 	return stringToChangeToUpperCase.upper();


# # print toUpperCase('kyle');

# # # Given a string, print the string reversed.

# # def reverse_string(string):
# # 	# let's split this string into an array

# # 	# string_array = list(string)	
# # 	# string_array.reverse()
# # 	# string_to_return = string_array.join(',')

# # 	print string[::-1]

# # reverse_string('rishi')


# # # Leetspeak

# # # Given a paragraph of text as a string, print the paragraph in leetspeak. To translate a string to leetspeak, you need to replace make the following character replacements (treat all input characters as uppercase):

# # # A => 4
# # # E => 3
# # # G => 6
# # # I => 1
# # # O => 0
# # # S => 5
# # # T => 7

# # leet_speak_dictionary = {

# # 	'A' : 4,
# # 	'E' : 3,
# # 	'G' : 6,
	
# # 	'I' : 1,
# # 	'O' : 0,
# # 	'S' : 5,
# # 	'T' : 7
	
# # }

# # # def convert_to_leet_speak(string):
# # # 	for letter in string:
# # # 		if letter in leet_speak_dictionary:
# # # 			print 'hi'

# # my_string ="human beings are interesting"
# # new_string = my_string

# # replacements = (  ('a','4'), ('e','3'), ('g','6'), ('i','1'), ('o', '0'), ('s', '5'), ('t', '7') )

# # for old, new in replacements:
# # 	new_string = new_string.replace(old, new)

# # print new_string
# # # Example: Leet => l337

# # # convert_to_leet_speak('human')

# # # 1 to 10

# # # Using a for loop and the range function, print out the numbers between 1 and 10 inclusive, one on a line. Example output:

# # # $ python 1_to_10.py
# # # 1
# # # 2
# # # 3
# # # 4
# # # 5
# # # 6
# # # 7
# # # 8
# # # 9
# # # 10

# # for i in range(1,11):
# # 	print i,


# # Same as the previous problem, except you will prompt the user for the number to start on and the number to end on. Example session:
# # $ python n_to_m.py
# # Start from: 2
# # End on: 8
# # 2
# # 3
# # 4
# # 5
# # 6
# # 7
# # 8

# # start = int(raw_input('pick a starting number, sir '))
# # end = int(raw_input('pick an ending number, sir '))


# # def counting(start, end):
# # 	for i in range(start, end+1):
# # 		print i


# # counting(start, end)


# # Print each odd number between 1 and 10 inclusive. Example output:

# # for i in range(1,11,2):
# # 	print i

# # Print a Square

# # Print a 5x5 square of * characters. Example output:

# # $ python square.py
# # *****
# # *****
# # *****
# # *****
# # *****




# # def create_square(number):
# # 	for i in range(1, number + 1):
# # 		print create_line_of_stars(number)
# # 	return " "

# # def create_line_of_stars(number):
# # 		for i in range(1, number+1):
# # 			print "*",
# # 		return " "

# # create_square(8)


# # Given an list of numbers, print their sum. When I say given something, just make something up and store it in a variable.



# # total = 0;
# # # for number in numbers:
# # # 	total += number
# # total = sum(numbers)

# # print total


# numbers = [5, 5, 5, 51, 23, 78, 56, -12, 1289, -35347281142890747890, 21211111991991, 29, 12, -1]
# # Given an list of numbers, print the largest of the numbers.

# # Given an list of numbers, print the smallest of the numbers.

# positive_numbers = []
# double_numbers = []


# for number in numbers:
# 	double_numbers.append(number * 2)




# print double_numbers


# Given an list of numbers, print each number in the list that is greater than zero.


# De-dup

# Given an list of numbers or strings, create a new list containing the same elements as the first list, except with any duplicate values removed. Print the list.

