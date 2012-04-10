import itertools
from math import sqrt

def get_triangle_number():
    for i in itertools.count(2,1):
        yield i*(i+1)/2
def get_factor_length():
    factor_length, largest_tri_number = 0,0
    triangle_numbers = get_triangle_number()
    for num in triangle_numbers:
        largest_tri_number = num
        factor_set = set(reduce(list.__add__, ([i, num/i] for i in range(1, int(sqrt(num)) + 1) if num % i == 0)))
        if len(factor_set) > 500:
            break
    print largest_tri_number

if __name__ == "__main__":
    get_factor_length()
