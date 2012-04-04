def problem3(n):
    '''The prime factors of 13195 are 5, 7, 13 and 29.
    
    What is the largest prime factor of the number 600851475143 ?'''
    factors = []
    div = 2
    if n%div==0:
        factors.append(2)
    div += 1
    while n > 2:
        if n%div==0:
            factors.append(div)
            n /= div
        div += 2
    return factors[-1]

if __name__ == "__main__":
    import sys
    print problem3(int(sys.argv[1]))
