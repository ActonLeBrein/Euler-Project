def primes_sieve(limit):
    limitn = limit+1
    not_prime = set()
    primes = []
    for i in range(2, limitn):
        if i in not_prime:
            continue
        for f in range(i*2, limitn, i):
            not_prime.add(f)
        primes.append(i)
    return primes

T = int(raw_input())
p = primes_sieve(104800)
for _ in range(T):
    print p[int(raw_input())-1]