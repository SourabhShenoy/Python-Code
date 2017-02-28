original = [[1,2,3,4],
			[5,6,7,8],
			[9,10,11,12],
			[13,14,15,16]]

c_op =[[13,9,5,1],
	 [14,10,6,2],
	 [15,11,7,3],
	 [16,12,8,4]]

a_op = [[4,8,12,16],
		[3,7,11,15],
		[2,6,10,14],
		[1,5,9,13]]

print(zip(*original[::-1]))

def rotate_clockwise(matrix, degree=90):
	if degree not in [0, 90, 180, 270, 360]:
		return None
	return matrix if not degree else rotate_clockwise(zip(*matrix[::-1]), degree-90)

print rotate_clockwise(original, 90)  

def rotate_counterclockwise(matrix, degree=90):
    if degree not in [0, 90, 180, 270, 360]:
        return None
    return matrix if not degree else rotate_counterclockwise(zip(*matrix)[::-1], degree-90)
 
print rotate_counterclockwise(original, 90)



def rotateMatrix(mat):
 
    if not len(mat):
        return
    top = 0
    bottom = len(mat)-1
 
    left = 0
    right = len(mat[0])-1
 
    while left < right and top < bottom:
 
        # Store the first element of next row,
        # this element will replace first element of
        # current row
        prev = mat[top+1][left]
 
        # Move elements of top row one step right
        for i in range(left, right+1):
            curr = mat[top][i]
            mat[top][i] = prev
            prev = curr
 
        top += 1
 
        # Move elements of rightmost column one step downwards
        for i in range(top, bottom+1):
            curr = mat[i][right]
            mat[i][right] = prev
            prev = curr
 
        right -= 1
 
        # Move elements of bottom row one step left
        for i in range(right, left-1, -1):
            curr = mat[bottom][i]
            mat[bottom][i] = prev
            prev = curr
 
        bottom -= 1
 
        # Move elements of leftmost column one step upwards
        for i in range(bottom, top-1, -1):
            curr = mat[i][left]
            mat[i][left] = prev
            prev = curr
 
        left += 1
 
    return mat
 
# Utility Function
def printMatrix(mat):
    for row in mat:
        print row
 
 
# Test case 1
matrix =[ 
            [1,  2,  3,  4 ],
            [5,  6,  7,  8 ],
            [9,  10, 11, 12 ],
            [13, 14, 15, 16 ]  
        ]
# Test case 2
"""
matrix =[
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
"""
 
matrix = rotateMatrix(matrix)
# Print modified matrix
printMatrix(matrix)