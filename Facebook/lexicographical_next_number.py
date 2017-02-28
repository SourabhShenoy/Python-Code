#TLE

def lexicalOrder(self, n):
    return sorted(range(1, n+1), key=str)
    
def lexicalOrder(self, n):
    return sorted(range(1, n+1), lambda a, b: cmp(str(a), str(b)))
    
    
#Faster. Shifting all numbers to whats present in N. Also, both are O(N)
def lexicalOrder(self, n):
    top = 1
    while top * 10 <= n:
        top *= 10
    def mycmp(a, b, top=top):
        while a < top: a *= 10
        while b < top: b *= 10
        return -1 if a < b else b < a
    return sorted(xrange(1, n+1), mycmp)