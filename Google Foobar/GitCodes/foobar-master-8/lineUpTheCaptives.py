from itertools import permutations
from math import factorial

""" 
You need to calculate the number of ways that rabbits can be lined up such that a
viewer on one end sees x rabbits, and a viewer on the other end sees y rabbits, because
some taller rabbits block the view of the shorter ones.

For example, if rabbits were arranged in line with heights 30 cm, 10 cm, 50 cm, 40 cm, and
then 20 cm, a guard looking from the left side would see 2 rabbits (30 and 50 cm) while
a guard looking from the right side would see 3 rabbits (20, 40, and 50 cm).

Write a method answer(x,y,n) which returns the number of possible ways to arrange n rabbits
of unique heights along an east to west line, so that only x are visible from the west, and
only y are visible from the east. The return value must be a string representing the number
in base 10.

If there is no possible arrangement, return "0".

The number of rabbits (n) will be as small as 3 or as large as 40.
The viewable rabbits from either side (x and y) will be as small as 1 and as large as
the total number of rabbits (n).

Inputs:
    (int) x = 2
    (int) y = 2
    (int) n = 3
Outputs:
    (string) "2"

Inputs:
    (int) x = 1
    (int) y = 2
    (int) n = 6
Outputs:
    (string) "24"

"""

first = [1,2,3,4,5]
final = [[e,j,i] for e,j,i in permutations(first,3) if e > j < i or e < j < i]





def findVariations(x,y,n):
    nlist = list(range(1,n+1))
    if x == 1:
        nlist.insert(0,nlist.pop())


    return nlist
    #peaks = list(range(x-1,n-y+1))



def answer2(x,y,n):
    count = 0
    if x == 1:
        if y == 1:
            return 1
        return answer2(x,y-1,n-1)    
    elif y == 1:
        if x == 1:
            return 1
        return answer2(x-1,y,n-1)
    else:
        # Places in line where the greatest value must be, the index of tallest individual cannot fall anywhere
        # in the line that is less than the value of x or greater than the n-y
        peaks = list(range(x-1,n-y+1))
        # the list peaks contains each index where the tallest individual could be placed
        count += len(peaks)
        # TO-DO work out way to recursively apply the above technique for each of the halves of the list, split
        # at the index of the peak. Find new greatest value in list and find permutations recursively.
        for i in peaks:
            new_list = list(range(1,i+1)) + [n] + list(range(i+1,n))
            count += answer2(x-1,y-1,n-1)
        return count

#print(variations(2,2,5))



mem = {}

def oneSide(n,k):
    if (n,k) in mem:
        return mem[(n,k)]
    elif k > n:
        mem[(n,k)] = 0
    elif k == n:
        mem[(n,k)] = 1
    elif k == 1:
        mem[(n,k)] = factorial(n-1)
    elif k == n-1:
        mem[(n,k)] = factorial(n) * (factorial(2)//factorial(n-2))
    else:
        mem[(n,k)] = oneSide(n-1,k-1) + oneSide(n-1,k) * (n-1)
    return mem[(n,k)]


def answer(x,y,n):
    combinations = lambda n,k: factorial(n) // (factorial(k) * factorial(n-k))
    return oneSide(n-1,x+y-2) * combinations(x+y-2,x-1)


print(answer(10,5,40))








