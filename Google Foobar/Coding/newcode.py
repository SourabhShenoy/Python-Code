def min_a(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)

def max_a(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return max(a, b)

def fin_solution(A, B, T):
    if T is None:
        return (0, 0, None, None)

    lef, left_size, left_min, _ = fin_solution(A, B, T.l)
    right, right_size, _, right_max = fin_solution(A, B, T.r)

    cur_size = 1 + left_size + right_size

    cmin = min_a(T.x, left_min)

    cmax = max_a(T.x, right_max)

    cur_ans = max_a(lef, right)
    if A <= cmin and cmax <= B:
        cur_ans = cur_size 

    return (cur_size, cur_ans, cmin, cmax)

def solution(A, B, T):
    res = fin_solution(A,B,T)
    return res[0]