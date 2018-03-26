def fact(n):
    factValue = 1
    for i in range(2,n+1):
        factValue = factValue * i
    return factValue

def binomial_coefficient(n,m):
    a = fact(n)
    b = fact(m)
    c = fact(n-m)
    return a//(c*b)

p = 10**9 + 7

T = int(raw_input())
for _ in xrange(T):
    N,M = map(int,raw_input().split(' '))
    print (binomial_coefficient(N+M,M)%p)