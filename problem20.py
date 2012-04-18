def factorial(n):
    if n==1:
        return 1
    else:
        return (n * factorial(n-1))

def sum_of_digits(n):
    num_as_str = str(n)
    return sum(int(x) for x in num_as_str)
    
if __name__ == "__main__":
    print sum_of_digits(factorial(100))
