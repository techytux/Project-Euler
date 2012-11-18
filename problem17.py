num_to_words = { 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 
				 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven",
				 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen",
				 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen",
				 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty"
				 70:"seventy", 80:"eighy", 90:"ninety", 100:"hundred"
				}

def get_word_for_number(num):
	div = 10
	while num > 1:
		digits = num%div
		num = num/div
		div *= 10