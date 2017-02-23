def findMutationDistance(start, end, bank):
    if end not in bank:
        return -1
        
    if start == end:
        return 0
        
    bank = [gene for gene in bank if gene != start]
    res = 0

    while start != end:
        legal_mut = []
        for gene in bank:
        	dist = sum(c1 != c2 for c1, c2 in zip(start, gene))
        	if dist == 1:
        		legal_mut.append(gene)

        if len(legal_mut) == 0:
            return -1

        if len(legal_mut) == 1:
            start = legal_mut[0]
            bank = [gene for gene in bank if gene != start]
        else:
            if end in legal_mut:
                return (res + 1)
            for ele in legal_mut:
                bank = [gene for gene in bank if gene != ele]
                res1 = findMutationDistance(ele, end, bank)
                if res1 != -1:
                    return (res + res1 + 1)

        res += 1

    return res

print findMutationDistance('AAAAAAAA', 'AAAAAATT', ['AAAAAAAA', 'AAAAAATT', 'AAAAAAAT', 'AAAAATTT'])
print findMutationDistance('AAAAAAAA', 'GGAAAAAA', ['GAAAAAAA', 'AAGAAAAA', 'AAAAGAAA', 'GGAAAAAA'])