#!/usr/bin/env python
from collections import deque


def getxy(src):
    return src / 8, src % 8


def bfs(sx, sy, mp):
    q = deque([(sx, sy)])
    while q:
        x, y = q.popleft()

        for dx in [-2, -1, 1, 2]:
            for dy in [-2, -1, 1, 2]:
                if abs(dx) == abs(dy):
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx <= 7 and 0 <= ny <= 7:
                    if mp[nx][ny] is None:
                        mp[nx][ny] = mp[x][y] + 1
                        q.append((nx, ny))


def answer(src, dest):
    # BFS
    mp = [[None for _ in xrange(8)] for _ in xrange(8)]
    sx, sy = getxy(src)
    dx, dy = getxy(dest)

    mp[sx][sy] = 0
    bfs(sx, sy, mp)
    return mp[dx][dy]


print answer(0, 1)
