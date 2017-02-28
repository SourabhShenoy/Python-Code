#2sum + 2sum = 4sum

def fourSum(self, num, target):
    two_sum = collections.defaultdict(list)
    res = set()
    for (n1, i1), (n2, i2) in itertools.combinations(enumerate(num), 2):
        two_sum[i1+i2].append({n1, n2})
    for t in list(two_sum.keys()):
        if not two_sum[target-t]:
            continue
        for pair1 in two_sum[t]:
            for pair2 in two_sum[target-t]:
                if pair1.isdisjoint(pair2):
                    res.add(tuple(sorted(num[i] for i in pair1 | pair2)))
        del two_sum[t]
    return [list(r) for r in res]