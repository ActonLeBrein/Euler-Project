def swap(i, j):                    
    sqc[i], sqc[j] = sqc[j], sqc[i] 

def heapify(end,i):   
    l=2 * i + 1  
    r=2 * (i + 1)   
    max=i   
    if l < end and sqc[i] < sqc[l]:   
        max = l   
    if r < end and sqc[max] < sqc[r]:   
        max = r   
    if max != i:   
        swap(i, max)   
        heapify(end, max)   

def heap_sort():     
    end = len(sqc)   
    start = end / 2 - 1
    for i in range(start, -1, -1):   
        heapify(end, i)   
    for i in range(end-1, 0, -1):   
        swap(i, 0)   
        heapify(i, 0)
        
N = int(raw_input())
sqc = []
name_scores = {}
for _ in xrange(N):
    sqc.append(raw_input())

heap_sort()
#print sqc
for j in xrange(len(sqc)):
    score = 0 
    for k in sqc[j]:
        score += ord(k) - 64
    name_scores[sqc[j]] = score * (j + 1)

#print name_scores
Q = int(raw_input())
for _ in xrange(Q):
    print name_scores[raw_input()]