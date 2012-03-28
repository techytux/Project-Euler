def sum_of_square(n):
    #mathematical formula n*(n+1)*(2*n +1)/6
    return n*(n+1)*(2*n +1)/6
def square_of_sum(n):
    # mathematical formula Sum of n natural numbers n/2 * (n+1)
    return (n/2*(n+1))**2

def problem6(n):
    return square_of_sum(n) - sum_of_square(n)

if __name__ == "__main__":
    import sys
    print problem6(int(sys.argv[1]))
    
