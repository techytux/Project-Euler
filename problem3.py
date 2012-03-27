def problem3(n):
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
    factors.sort(reverse=True)
    return factors[0]

if __name__ == "__main__":
    import sys
    print problem3(int(sys.argv[1]))
