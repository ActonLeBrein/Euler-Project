import math

phi_pos = (1+math.sqrt(5)) / 2
phi_neg = (1-math.sqrt(5)) / 2
phi = phi_pos**3
psi = phi_neg**3

def Fib_Inv_Log(n):
    return int(round(math.log((n*math.sqrt(5) + math.sqrt(5*(n**2)+4))/2,phi_pos)))

def Fib_Inv(n):
    return int(round((math.log(n*(math.sqrt(5))) / math.log(phi_pos))))

def Fn(n):
    return int(round((phi_pos**n - phi_neg**n)/math.sqrt(5)))

def Fib_Even(k):
    return int(round((1/math.sqrt(5)) * ((phi * ((1 - phi**k) / (1 - phi))) + (psi * ((1 - psi**k) / (1 - psi))))))

T = int(raw_input())
for _ in range(T):
    sum_t = 0
    n = int(raw_input())
    v = Fib_Inv_Log(n)
    if (Fn(v) == n) and (v%3 == 0):
        sum_t = Fib_Even(v/3)
    elif Fn(v) == n:
        pass
    elif Fn(v) < n:
        pass
    else:
        while Fn(v) > n:
            v = v - 1
            if Fn(v) == n:
                break
            elif Fn(v) < n:
                break
            else:
                pass
    if v%3 == 1:
        v = v - 1
    elif v%3 == 2:
        v = v - 2
    else:
        pass
    sum_t = Fib_Even(v/3)
    print sum_t