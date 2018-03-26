def factors(n):
    l = reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))
    l.remove(n)
    return sum(l)

def amicable(number):
    answer = []
    for x in range(4, number):
        if x in answer:
            continue
        a = factors(x) 
        if a > 4:
            b = factors(a)
            if b == x and a != x:
                answer.append(x)
                answer.append(a)
            else:
                continue
        else:
            continue
    return answer

amicable_list = amicable(10**5)
#print amicable_list

T = int(raw_input())
for _ in xrange(T):
    N = int(raw_input())
    A = 0
    for j in xrange(len(amicable_list)):
        if amicable_list[j] < N:
            A += amicable_list[j]
        else:
            continue
    print A