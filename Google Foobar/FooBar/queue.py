def answer(start, length):
    xsum = 0
    for i in range(length):
        rstart = start + (i * length)
        rend = rstart + length
        xsum ^= xor(rstart, rend) ^ xor(rend - i,  rend)

    return xsum

def xor(a, b):
    if a == 0:
        if b % 4 == 0: 
            return b
        elif b % 4 == 1:
            return 1
        elif b % 4 == 2:
            return b + 1
        else: 
            return 0
    else:
        return xor(0, a - 1) ^ xor(0, b)
        
print(answer(17,4))