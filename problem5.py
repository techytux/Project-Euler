def is_divisible(number):
    for i in range(11, 21):
        if number%i != 0:
            return False
    return True

if __name__ == "__main__":
    import itertools
    # Since 2520 is divisible by all numbers up to 10.
    # The new number has to be divisible by 2520
    i = 2520
    while True:
        if is_divisible(i):
            print i
            break
        i += 2520
