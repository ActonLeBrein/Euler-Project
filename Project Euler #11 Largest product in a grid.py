def diagonal(m):
    max_val = 0
    h = 0
    v = 0
    dr = 0
    dl = 0
    for y in xrange(20):
        for x in xrange(20):
            if y <= 16 and x <= 16:
                if dr < m[y][x]*m[y+1][x+1]*m[y+2][x+2]*m[y+3][x+3]:
                    dr = m[y][x]*m[y+1][x+1]*m[y+2][x+2]*m[y+3][x+3]
                    
                if dl < m[y][x+3]*m[y+1][x+2]*m[y+2][x+1]*m[y+3][x]:
                    dl = m[y][x+3]*m[y+1][x+2]*m[y+2][x+1]*m[y+3][x]
                    
                if h < m[y][x]*m[y][x+1]*m[y][x+2]*m[y][x+3]:
                    h = m[y][x]*m[y][x+1]*m[y][x+2]*m[y][x+3]
                    
                if v < m[y][x]*m[y+1][x]*m[y+2][x]*m[y+3][x]:
                    v = m[y][x]*m[y+1][x]*m[y+2][x]*m[y+3][x]
                    
            elif y <= 16 and x >= 16:
                if v < m[y][x]*m[y+1][x]*m[y+2][x]*m[y+3][x]:
                    v = m[y][x]*m[y+1][x]*m[y+2][x]*m[y+3][x]
                    
            elif y >= 16 and x <= 16:
                if h < m[y][x]*m[y][x+1]*m[y][x+2]*m[y][x+3]:
                    h = m[y][x]*m[y][x+1]*m[y][x+2]*m[y][x+3]
    val = [h,v,dr,dl]
    max_val = max(val)
    return max_val              

M = []

for _ in xrange(20):
    M.append(map(int,raw_input().split(' ')))
    
print diagonal(M)