# At most x 4s, y 5s and z 6s. Find sum of all possible combinations of these numbers and return sum modulo 10^9 + 7

def getSum(x,y,z,num):
    numX,numY,numZ=0,0,0;
    if x==0 and y==0 and z==0:
        return 0
    if x!=0:
        numX=num*10+4
        numX+=getSum(x-1,y,z,numX)
    if y!=0:
        numY=num*10+5
        numY+=getSum(x,y-1,z,numY)
    if z!=0:
        numZ=num*10+6
        numZ+=getSum(x,y,z-1,numZ)
    return numX+numY+numZ
    
testcase=int(raw_input())

while testcase>0:
    testcase-=1
    inp=map(int,raw_input().split())
    x=inp[0]
    y=inp[1]
    z=inp[2]
    print getSum(x,y,z,0)%(10**9+7)