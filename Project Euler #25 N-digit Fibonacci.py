def fibo(n):
    a, b, p, q = 1, 0, 0, 1
    while n > 0:
        if n % 2 == 0:
            oldp = p
            p = p*p + q*q
            q = 2*oldp*q + q*q
            n //= 2
        else:
            olda = a
            a = b*q + a*q + a*p
            b = b*p + olda*q
            n -= 1
    return b
    
l1 = 0
d = 0
i = 1
flag = True
counts = {}
while flag:
    a = fibo(i)
    l2 = len(str(a))
    if l2 == 5001:
        flag = False
    elif l1 < l2:
        l1 = l2
        #print 'Fib pos {0}, Difference {1}, Length {2}, Fib {3}'.format(i,i-d,l2,a)
        counts[l2] = i
        d = i
    i += 1
#print counts

T = int(raw_input())
for _ in xrange(T):
    N = int(raw_input())
    print counts[N]