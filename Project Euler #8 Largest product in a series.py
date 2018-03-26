import operator
import functools

def large_product(l,k):
    maxi = 0
    for i in range(len(l)-k-1):
        ans = functools.reduce(operator.mul, l[i:i+k], 1)
        if ans > maxi:
            maxi = ans
        else:
            continue
    return maxi

T = int(raw_input())
for _ in range(T):
    a,b = map(int, raw_input().split(' '))
    c = map(int, list(raw_input()))
    print large_product(c,b)