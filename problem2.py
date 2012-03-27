def problem2(range):
    a,b,sum = 1,2,0
    while a < range:
        if a%2==0:
            sum += a
        a,b = b, a+b
    return sum

if __name__ == "__main__":
    import sys
    print problem2(int(sys.argv[1]))
