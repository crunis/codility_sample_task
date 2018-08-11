## APPROACH 2

class Range:
    low = 0
    high = 0
    
    next_range = None
    prev_range = None
    
    def __init__(self, n):
        self.low=self.high=n
        
    def __str__(self):
        return "(%s, %s)" % (self.low, self.high)


def solution(A):
    r = Range(0)
    
    for n in A:
        curr = r
        while True:
            print("(%s, %s)" % (curr.low, curr.high))
            if not curr.next_range:
                break
            curr = curr.next_range
        print(" >>> %s " % n)
        if n < 1:
            continue
        
        action = False
        curr = r
        while True:
            if curr.low <= n and curr.high >= n:
                print("absorbed")
                action = True
            if curr.high == n-1:
                print("enlarging")
                action = True
                curr.high = n
                if curr.next_range and curr.next_range.low == n + 1:
                    print("connecting")
                    curr.high = curr.next_range.high
                    curr.next_range = curr.next_range.next_range
            if curr.low > n:
                r2 = Range(n)
                r2.next_range = curr
                curr.prev_range.next_range = r2
                curr.prev_range = r2
                print("inserting")
                action = True
                
            if action:
                break
            
            if not curr.next_range:
                break
            
            curr=curr.next_range

        if not action:
            r3 = Range(n)
            r3.prev_range = curr
            r3.next_range = curr.next_range
            curr.next_range = r3
            print("appending")
        
    curr = r
    while True:
        print("(%s, %s)" % (curr.low, curr.high))
        if not curr.next_range:
            break
        curr = curr.next_range
    
    return r.high + 1
    
