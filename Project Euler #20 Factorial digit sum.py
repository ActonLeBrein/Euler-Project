T = int(raw_input())

for _ in xrange(T):
    N = int(raw_input())
    fact = 1
    for i in xrange(1,N+1):
        fact = fact * i
    print sum(map(int,list(str(fact))))