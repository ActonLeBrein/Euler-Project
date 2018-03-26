from math import factorial, floor

def nthperm(S, k):
    P = []
    while len(S) > 0:
        f = factorial(len(S)-1)
        i = int(floor(k/f))
        x = S[i]
        k = k%f
        P.append(x)
        S = S[:i] + S[i+1:]
    return ''.join(P)

T = int(raw_input())
for _ in xrange(T):
    N = int(raw_input())
    print nthperm('abcdefghijklm',N-1)