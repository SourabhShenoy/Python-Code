from collections import deque

def bfs(maze, x, y):
	row = len(maze)
	col = len(maze[0])
	score = [[None for j in range(col)] for i in range(row)]
	
	deq = deque([(x,y,1)])

	while deq:
		x,y,val = deq.popleft()
		if score[x][y] is not None:
			continue

		score[x][y] = val
		
		if maze[x][y] == 1:
			continue
		
		for a,b in [[1,0],[-1,0],[0,1],[0,-1]]:
			new_x = x + a
			new_y = y + b
			
			if row > new_x >= 0 and col > new_y >= 0:
				new_x = x + a
				new_y = y + b
				if new_x >=0 and new_x < row and new_y >=0 and new_y < col:
					if score[new_x][new_y] is None:
						deq.append((new_x, new_y, val + 1))
	return score


def answer(maze):
    row = len(maze)
    col = len(maze[0])
    start = bfs(maze, 0, 0)
    end = bfs(maze, row - 1 , col - 1)
    res = 2 << 32

#    start = [[1,2,5,None],[2,3,4,5],[3,4,5,6],[None,None,6,7]]
#    end = [[7,6,5,None],[6,4,5,3],[7,4,3,2],[None,None,2,1]]
    row = len(maze) - 1
    col = len(maze[0]) - 1   
    
    while row != -1:
        col = len(maze[0]) - 1
    	while col != -1:
			if start[row][col] is not None and end[row][col] is not None:
				res = min(start[row][col] + end[row][col] - 1, res)
			col -= 1
    	row -= 1
    return res


maze = {}
maze[0] = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
maze[1] = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
maze[2] = [[0,0,0,0,0,0],[1,1,1,1,1,0],[1,1,1,1,0,0],[1,0,1,1,1,1],[1,1,1,1,0,1],[0,0,0,0,0,1]]
for i in range(len(maze)):
    print(answer(maze[i]))
