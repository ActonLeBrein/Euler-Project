import math

def P_T(N):
    max_val = -1
    for a in range(1,N):
        b = (((N*N)/2)-(N*a))/(N-a)
        c = N-a-b
        if isinstance(b, int) and (a**2 + b**2 == c**2) and (a<b<c):
            if max_val < a*b*c:
                max_val = a*b*c
    return max_val

T = int(raw_input())
for _ in range(T):
    print P_T(int(raw_input()))