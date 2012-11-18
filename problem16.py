def problem16():
    number = str(2**1000)
    number_as_list = list(number)
    return sum(int(x) for x in number_as_list)
if __name__ == "__main__":
    print "the sum of digits are:",problem16()
