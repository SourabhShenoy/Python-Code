"""
Binary Bunnies
--------------

To make your binary tree, the rabbits were sorted by their ages (in days) and each, luckily
enough, had a distinct age. For a given group, the first rabbit became the root, them the 
next one (taken in order of rescue) was added, older ages to the left and younger to the right.
The order that the rabbits returned to you determined the end pattern of the tree, and herein
lies the problem. 

Since the tree did not preserve the order of rescue, it falls to you to figure out how many
different sequences of rabbits could have produced an identical tree to your same sequence, 
so you can keep all the rescued rabbits safe. 

For example, if the rabbits were processed in order from [5, 9, 8, 2, 1], it would result
in a binary tree identical to one created from [5,2,9,1,8].

You must write a function answer(seq) that takes an array of up to 50 integers and returns a
representing the number (in base-10) of sequences that would result in the same tree as the
given sequence. 

Inputs:
    (int list) seq = [5,9,8,2,1]
Outputs:
    (string) "6"

Inputs:
    (int list) seq = [1,2,3,4,5,6,7,8,9,10]
Outputs:
    (string) "1"

"""

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

def nchoosek(n, k):
    if 0 <= k <= n:
        return (factorial(n))/(factorial(k)*factorial(n-k))

def answer(seq):
    if len(seq) == 0:
        return 1
    else:
        root = seq[0]
        left_subtree = [i for i in seq[1:] if i > root]
        right_subtree = [i for i in seq[1:] if i < root]

        tree = [root, 2 * answer(left_subtree), 2 * answer(right_subtree)]

        m = len(left_subtree)
        n = len(right_subtree)
        number_of_ways = nchoosek(m+n,m) * answer(left_subtree) * answer(right_subtree)
        return int(number_of_ways)


print(answer([5,2,1,9,8]))
print(answer([5,3,7,2,4,6,9]))
print(answer([1,2,3,4,5,6,7,8,9,10]))




