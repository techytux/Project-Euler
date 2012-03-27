def is_palindrome(number):
    number_to_str = str(number)
    length_of_number = len(number_to_str)
    for i in range(0, length_of_number/2):
        if number_to_str[i]!=number_to_str[(-i-1)]:
            return False
    return True 

def product():
    best = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            num = i*j
            if is_palindrome(i*j) and num > best:
                best = num
    return best

if __name__ == "__main__":
    import sys
    print product() 
