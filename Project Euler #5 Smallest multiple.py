import operator
import functools

def cf(n):
    l1 = list(range(1,n+1))
    l2 = []
    for i in range(len(l1)):
        if l1[i] != 1:
            l2.append(l1[i])
            for j in range(len(l1)):
                if l1[j] == 1:
                    pass
                elif l1[j]%l2[-1] == 0:
                    l1[j] =l1[j]/l2[-1]
                else:
                    pass
        else:
            pass
    res = functools.reduce(operator.mul, l2, 1)
    return res
            
T = int(raw_input())
for _ in range(T):
    print cf(int(raw_input()))