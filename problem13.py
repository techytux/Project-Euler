import itertools

def get_number():
	with open("numberlist.txt", 'r') as number_list:
		lines = number_list.readlines()
		for line in lines:
			yield int(line)

if __name__ == "__main__":
	print str(sum(get_number()))[:10]

	