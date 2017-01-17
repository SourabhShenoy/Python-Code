
from itertools import product

# def get_combos_0_1(n, parity):
#     permutes = []

#     if parity:
#         for i in range(1,n,2):
#             new = [1]*i + ([0]*((n-1)-i))
#             permutes += list(set(permutations(new)))
#     else:
#         for i in range(0,n,2):
#             new = [1]*i + ([0]*((n-1)-i))
#             permutes += list(set(permutations(new)))
#     return [list(i) for i in permutes]


def toggle_even(grid):
    points = []
    for i in range(len(grid)):
        if 1 in grid[i]:
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    points.append([i,j])
    for i in points:
        row = i[0]
        column = i[1]
        for j in range(len(grid[row])):
            if j != column:
                grid[row][j] += 1
        for k in range(len(grid)):
            if k != row:
                grid[k][column] += 1
    
    total_moves = 0
    for i in range(len(grid)):
        grid[i] = [c%2 for c in grid[i]]
        total_moves += sum(grid[i])

    return total_moves



def toggle_odd(grid):
    row_parity = []
    column_parity = []
    for i in range(len(grid)):
        row_parity.append(sum(grid[i]))
        column_sum = 0
        for j in range(len(grid)):
            column_sum += grid[j][i]
        column_parity.append(column_sum)
    if row_parity[0] % 2 == 0:
        odd_parity = False
        for i in row_parity[1:]:
            if i % 2 != 0:
                return -1
        for i in column_parity:
            if i % 2 != 0:
                return -1
    else:
        odd_parity = True
        for i in row_parity[1:]:
            if i % 2 == 0:
                return -1
        for i in column_parity:
            if i % 2 == 0:
                return -1


    return 1


def answer(grid):
    if len(grid) % 2 == 0:
        return toggle_even(grid)
    return toggle_odd(grid)



grid1 = [[0,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
grid2 = [[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,0]]
grid3 = [[1,1],[0,0]]
grid4 = [[1,1,0,1,0],[0,1,0,0,0],[1,1,1,0,0],[1,0,0,1,1],[0,0,0,1,0]]
grid5 = [[0,1,0],[0,0,1],[0,0,1]]

print(answer(grid4))





