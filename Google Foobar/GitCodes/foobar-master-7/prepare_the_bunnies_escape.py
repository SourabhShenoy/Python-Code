#!/usr/bin/env python
from collections import deque


def bfs(maze, sx, sy):
    M, N = len(maze), len(maze[0])
    score = [[None for _ in xrange(N)] for _ in xrange(M)]

    cnt = 0
    q = deque([(sx, sy, 1)])
    while q:
        cnt += 1
        x, y, k = q.popleft()
        if score[x][y] is not None:
            continue

        score[x][y] = k
        if maze[x][y] == 1:
            continue

        for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x + i, y + j
            if 0 <= nx < M and 0 <= ny < N:
                if score[nx][ny] is None:
                    q.append((nx, ny, k + 1))

    return score


def answer(maze):
    M, N = len(maze), len(maze[0])
    a1 = bfs(maze, 0, 0)
    a2 = bfs(maze, M - 1, N - 1)

    ans = 2 << 32
    for i in xrange(M):
        for j in xrange(N):
            if a1[i][j] and a2[i][j]:
                ans = min(a1[i][j] + a2[i][j] - 1, ans)
    return ans


if __name__ == '__main__':
    size = 20
    print answer([[0 for _ in xrange(size)] for _ in xrange(size)])
