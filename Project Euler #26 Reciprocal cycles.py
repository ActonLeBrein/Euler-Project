# Enter your code here. Read input from STDIN. Print output to STDOUT

def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n//2) if sieve[i]]

def reciprocal_cycles(N):
    if N < 8: return 3
    for d in prime_sieve(N)[::-1]:
        period = 1
        while pow(10, period) % d != 1: period += 1
        if d-1 == period: return d

T = int(raw_input())

for _ in xrange(T):
    print reciprocal_cycles(int(raw_input()))