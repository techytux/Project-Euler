import itertools

def gen_next_number(n):
	if n % 2 == 0:
		return n / 2
	else:
		return 3*n + 1

def gen_series(num):
	count = 1
	while num != 1:
		num = gen_next_number(num)
		count += 1 
	return count

if __name__ == "__main__":
	max = 1
	max_list = []
	
	for i in xrange(13, 1000000):
		if gen_series(i) >= max:
			max_list.append(i)
			max = gen_series(i)
	
	print "max", max_list[-1]