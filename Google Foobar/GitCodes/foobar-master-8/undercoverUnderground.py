from math import factorial


"""
There are abandoned tunnels between the warrens of the rabbits, and you need to find the best
way to use them. In some cases, Beta Rabbit wants a high level of interconnectedness, especially
when the groups show their loyalty and worthiness. In other scenarios the groups should be less
intertwined, in case there any are compromised by enemy agents or zombits.

Every warrent must be connected to every other warren somehow, and no two warrens should ever
have more than one tunnel between them. Count the number of ways to connect the resistance
warrens. 

For example, with 3 warrens (denoted A,B,C) and 2 tunnels, there are three distinct ways to
connect them:

A-B-C
A-C-B
C-A-B

With 4 warrens and 6 tunnels, the only way to connect them is to connect each warren to every
other warren. 

Write a function answer(n,k) which returns the number of ways to connect N distinctively
labelled warrens with exactly k tunnels, so that there is a path between any two warrens.
n will be at least 2 and at most 20. k will be at least one less than n and at most ((n*(n-1))/2.


"""

"""
This function uses analytic combinatorics to recursively find the sum. The binomial coefficient 
is an important piece to the puzzle and is used frequently throughout the algorithm. 

By utilizing dictionaries to memoize computed items, the program becomes dramatically faster. 
With the time to compute every possible value in the given range ~0.8-0.9 seconds. 


"""


bin_dict = {}

def binCoefficient(n,k):
    if (n,k) in bin_dict:
        return bin_dict[(n,k)]
    else:
        if n < k:
            result = 0
        elif k == 0 or n == k:
            result = 1
        elif k == 1 or k == n-1:
            result = n
        else:
            result = factorial(n)/(factorial(k)*factorial(n-k))
        bin_dict[(n,k)] = result
        return bin_dict[(n,k)]


answer_dict = {}

def generateAnswers(n,k):
    if (n,k) in answer_dict:
        return answer_dict[(n,k)]

    elif k == n-1:
            all_graphs = int(n**(n-2))

    else:
        maximum_edges = n*(n-1)>>1

        if k == maximum_edges:
            all_graphs = 1

        else:
            all_graphs = binCoefficient(maximum_edges,k)

            if k < maximum_edges-n+2:
                for i in range(1,n):
                    x = binCoefficient(n-1,i-1)
                    minimum_vertices = min(i*(i-1)>>1, k)

                    for j in range(i-1,minimum_vertices+1):
                        all_graphs -= x * binCoefficient(binCoefficient(n-i,2),k-j) * generateAnswers(i,j)

    answer_dict[(n,k)] = int(all_graphs)
    return answer_dict[(n,k)]


def answer(n,k):
    return str(generateAnswers(n,k))


print(answer(5,4))




