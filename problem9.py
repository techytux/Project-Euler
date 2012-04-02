def problem9():
    for a in range(1, 500):
        for b in range(1, 500):
            c = 1000 - a - b
            if a<b<c:
                is_triplet = a**2 + b**2 == c**2
                if is_triplet:
                    print a*b*c
                    break

if __name__ == "__main__":
    problem9()
    
