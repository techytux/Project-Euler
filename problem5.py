def is_divisible(number):
    for i in range (1, 20):
        if number%i != 0:
            return False
    return True

if __name__ == "__main__":
    import itertools
    for i in itertools.count(1):
        if is_divisible(i):
            print i
            break
