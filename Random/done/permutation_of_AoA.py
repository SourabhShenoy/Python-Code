"""
l = [[1,2,3],[4],[5,6,7]]
print (reduce(lambda a,b: [str(i)+str(j) for i in a for j in b], l))
"""

import itertools
print(list(itertools.product("abc", "ab", "ghrw")))
