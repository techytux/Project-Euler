import itertools

def gen_primes(upper_bound):
    d = {}
    q = 2
    while q < upper_bound:
        if q not in d:
            yield q
            d[q*q] = [q]
        else:
            for p in d[q]:
                d.setdefault(p+q, []).append(p)
            del d[q]
        q += 1


if __name__ == "__main__":
    prime_list = list()
    upper_bound = 2000000
    #for i in gen_primes(upper_bound)
    #    prime_list.append(i)
    print sum(gen_primes(upper_bound))
