def factors(n):
    l = reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))
    l.remove(n)
    return sum(set(l))

def abundant_sum(number):
    abundants = [0]*(number+1)
    for x in range(1,number+1):
        if factors(x) > x:
            abundants[x] = 1
        else:
            continue
    return abundants

def check(n,s):
    c1 = 0
    while c1 < len(s):
        c2 = c1 + 1
        while c2 < len(s):
            if s[c1] + s[c2] == n:
                return 'YES'
            else:
                c2 += 1
        c1 += 1
    return 'NO'

abundant_sum_list = abundant_sum(28123)
#print abundant_sum_list
T = int(raw_input())
for _ in xrange(T):
    N = int(raw_input())
    S = [i for i in xrange(len(abundant_sum_list[:N])) if abundant_sum_list[i] == 1]
    if N < 12:
        print 'NO'
    elif N > 28123:
        print 'YES'
    elif N in map(lambda x: 2*x ,S):
        print 'YES'
    else:
        print check(N,S)