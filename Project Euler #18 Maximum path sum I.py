def max_path(tri):
    while len(tri) > 1:
        t0 = tri.pop()
        t1 = tri.pop()
        #print t0,t1
        tri.append([max(t0[i], t0[i+1]) + t for i,t in enumerate(t1)])
        #print tri
    return tri[0][0]    

T = int(raw_input())
for _ in xrange(T):
    N = int(raw_input())
    tri = []
    for _ in xrange(N):
        tri.append(map(int,str(raw_input()).split(' ')))
    print max_path(tri)