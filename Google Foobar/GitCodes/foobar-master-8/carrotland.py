from fractions import gcd

"""
You want to plant as many carrots as you can. But you also want to follow these
guidelines: The carrots may only be planted at points with integer coordinates on the
2-D plane. They must lie within the plot of land and not on the boundaries. For example, if
the vertices were (-1,-1), (1,0) and (0,1), then you can only plant one carrot at (0,0)

Write a function answer(vertices), which, when given a list of three vertices, returns
the maximum number of carrots you can plant.

The vertices list will contain exactly three elements, and each element will be a list of
two integers representing the x and y coordinates of a vertex. All coordinates will have
absolute value no greater than 1000000000. The three vertices will not be collinear.

Inputs:
    (int) vertices = [[2,3],[6,9],[10,160]]
Output:
    (int) 289

Inputs:
    (int) vertices = [[91207, 89566], [-88690,-83026],[67100,47194]]
Output:
    (int) 1730960165

"""

def getArea(v0,v1,v2):
    a = abs(((v0[0]*(v1[1]-v2[1])) + (v1[0]*(v2[1]-v0[1])) + (v2[0]*(v0[1]-v1[1])))/2)
    return a

# Integer points on boundaries
def getB(v0,v1,v2):
    first = gcd(abs(v0[0]-v1[0]),abs(v0[1]-v1[1]))
    second = gcd(abs(v1[0]-v2[0]), abs(v1[1]-v2[1]))
    third = gcd(abs(v2[0]-v0[0]), abs(v2[1]-v0[1]))
    print(first,second,third)
    return first+second+third


def answer(vertices):
    v1,v2,v3 = vertices
    b = getB(v1,v2,v3)
    area = getArea(v1,v2,v3)
    i = area - (b/2) + 1
    return int(i)

print(answer([[0,0],[0,4],[12,0]]))
print(answer([[91207, 89566], [-88690,-83026],[67100,47194]]))





