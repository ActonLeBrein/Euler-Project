def power_2(n):
    if n == 0:
        return 1
    else:
        return 2**n

def fast_power(n):
    ans = 1
    if n%2 == 0:
        a = power_2(n/2)
        return a * a
    else:
        a = power_2(n/2)
        return a * a * 2
        
def power_2_sum(n):
    a = fast_power(n)
    b = sum(map(int,(list(str(a)))))
    return b

T = int(raw_input())

for _ in xrange(T):
    N = int(raw_input())
    print power_2_sum(N)