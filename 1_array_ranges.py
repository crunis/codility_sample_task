class Range:
    low = 0
    high = 0
    
    def __init__(self, n):
        self.low=self.high=n
        
    def __str__(self):
        return "(%s, %s)" % (self.low, self.high)


def solution(A):
    data = [Range(0)]
    for n in A:
        print(" >>> %s " % n)
        if n < 1:
            continue
        
        action = False
        for d in range(len(data)):
            if data[d].low <= n and data[d].high >= n:
                print("absorbed")
                action = True
            if data[d].high == n-1:
                print("enlarging")
                action = True
                data[d].high = n
            if data[d].low > n:
                data.insert(d, Range(n))
                print("inserting")
                action = True
                
            if len(data) > d+1 and data[d+1].low == n+1:
                data[d].high=data[d+1].high
                del data[d+1]
                print("connecting")
            
            if action:
                break

        
        if not action:  
            data.append(Range(n))
            print("appending")
        
    for d in data:
        print(d)
    
    return data[0].high + 1
    
