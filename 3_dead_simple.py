def solution(A):
    d = [False] * 1000001
    d[0] = True
    
    for n in A:
        if n < 1:
            continue
        
        d[n] = True
    
    for n in range(1000000):
        if not d[n]:
            return n
