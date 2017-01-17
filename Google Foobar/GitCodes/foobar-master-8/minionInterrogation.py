from itertools import permutations

"""
You decide to interrogate minions in an order which will take the least
expected time. For example, you have capture two minions: minion A
takings 10 minutes, and giving the answer with probability 1/2, and
minon B taking 5 minutes, but giving the answer with probability 1/5.

If you interrogation A first, then you expect to take 12.5 minutes. If
you interrogate B first, then you expect to take 13 minutes and thus
you must interrogate A first for the shortest expected time for getting
the answer.

Write a function answer(minions) which given a list of the
characteristics of each minion, returns the lexicographically smallest
ordering of minions, which gives you the smallest expected time of
confirming the password

The minions are numbered starting from 0. The minions parameter will
be a list of lists. minions[i] will be a positive integer representing
the time the machine takes for that minion.

The ratio of the second and third elements will be the probability of
that minion giving you the answer: the second element, a positive integer,
will be the numerator of the ratio and the third element, also a positive
integer will be the denominator of the ratio. The denominator will always
be greater than the numerator.

The return value must be a list of minion numbers depicting the optimal
order in which to interrogate the minions. Since there could be 
multiple optimal orderings, return the lexicographically first optimal
list.

Inputs:
minions = [[5,1,5],[10,1,2]]

Outputs:
[1,0]

Inputs:
minions = [[390,185,624],[686,351,947],[276,1023,1024],[199,148,250]]

Outputs:
[2,3,0,1]

"""


def answer(minions):
    minions = [m[0]/(m[1]/m[2]) for m in minions]
    minions_length = len(minions)
    minion_orders = sorted(range(minions_length), key=minions.__getitem__)
    return minion_orders


print(answer([[5,1,5],[10,1,2]]))
print(answer([[390,185,624],[686,351,947],[276,1023,1024],[199,148,250]]))











