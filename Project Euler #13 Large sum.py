N = 0
T = int(raw_input())
for _ in xrange(T):
    N = N + long(raw_input())
    
print long(str(N)[0:10])