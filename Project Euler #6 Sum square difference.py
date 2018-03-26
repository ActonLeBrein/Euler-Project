def sum_power(n):
    s1 = ((n**2 + n)/2)**2
    s2 = (2*n**3 + 3*n**2 + n)/6
    res = abs(s2-s1)
    return res

T = int(raw_input())

for _ in range(T):
    print sum_power(int(raw_input()))
