def problem1(number):
    sum = 0
    for i in range(number):
        if i%3==0 or i%5==0:
            sum += i
    return sum

if __name__ == "__main__":
    import sys
    print problem1(int(sys.argv[1]))
