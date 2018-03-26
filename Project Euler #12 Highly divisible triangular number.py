def triangular(m):
    return (m*(m+1))/2

def num_of_factors(n):
    result_set = set()
    for i in range(1, 1+int(n**0.5)):
        if n % i == 0:
            result_set.add(n // i)
            result_set.add(i)
    return len(result_set)

def tri_fact(n):
    t = n*(n+1)*1/2
    if n%2 == 0:
        f = num_of_factors(n/2)*num_of_factors(n+1)
    else:
        f = num_of_factors(n)*num_of_factors((n+1)*1/2)
    return t,f

t = []
d = 1
val = tri_fact(d)
for k in xrange(1,1002):
    while val[1] < k:
        val = tri_fact(d)
        d += 1
    t.append(val[0])

T = int(raw_input())
for _ in xrange(T):
    N = int(raw_input())
    print t[N]