def primes_sieve(n):
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

T = int(raw_input())
p = primes_sieve(10**6)
s = 0
j = 0
l = []
for k in xrange(1,10**6):
    if j > len(p)-1:
        break
    elif k < p[j]:
        l.append(s)
    else:
        s = s + p[j]
        j += 1
        l.append(s)
        
for _ in range(T):
    N = int(raw_input())
    print l[N-1]