def answer(n):
    res = [[0 for _ in range(n)] for _ in range(n + 1)]

    for i in range(3):
        for j in xrange(i, n):
            res[i][j] = 1

    for i in range(3, n + 1):
        for j in range(2, n):
            res[i][j] = res[i][j - 1]
            if i >= j:
                res[i][j] += res[i - j][j - 1]

    return res[n][n - 1]