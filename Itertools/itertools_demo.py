# itertools.product()

# This tool computes the cartesian product of input iterables. 
# It is equivalent to nested for-loops. 
# For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

from itertools import product

res1 = list(product([1,2,3], repeat=2))
print (res1)
# [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

A =[[1,2,3],[7,8,9]]
res2 = (list(product(*A)))
print(res2)
# [(1, 7), (1, 8), (1, 9), (2, 7), (2, 8), (2, 9), (3, 7), (3, 8), (3, 9)]

B = [[1,2,3],[4,5,6],[7,8,9]]
res3 = list(product(*B))
print(res3)
type(res3)
# [(1, 4, 7), (1, 4, 8), (1, 4, 9), (1, 5, 7), (1, 5, 8), (1, 5, 9), 
#(1, 6, 7), (1, 6, 8), (1, 6, 9), (2, 4, 7), (2, 4, 8), (2, 4, 9), (2, 5, 7), (2, 5, 8), (2, 5, 9), (2, 6, 7), (2, 6, 8), (2, 6, 9), (3, 4, 7), 
#(3, 4, 8), (3, 4, 9), (3, 5, 7), (3, 5, 8), (3, 5, 9), (3, 6, 7), (3, 6, 8), (3, 6, 9)]
# list

C = [1,2,3]
D =[3,4]
res4 = list(product(C,D))
print (res4)
# [(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]
==================================================================================================================================================================

# No need to use quotes for numbers, but we need to use 
# quotes for alphabets while using permutation

from itertools import permutations

res5 = list(permutations([1,2,3]))
print(res5)
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

res6 = list(permutations([2,3,4],2))
print(res6)
# [(2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3)]

res7 = list(permutations(['a','b','c'],2))
print(res7)
#[('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]
==================================================================================================================================================================

from itertools import combinations

print (list(combinations(['a','g','m'],2)))
# [('a', 'g'), ('a', 'm'), ('g', 'm')]

A = [1,9,3,4]
print (list(combinations(A,2)))
# [(1, 9), (1, 3), (1, 4), (9, 3), (9, 4), (3, 4)]
==================================================================================================================================================================
from itertools import combinations
from itertools import combinations_with_replacement

word, num = input().split()

res1 = list(combinations(sorted(word),int(num)))
res2 = list(combinations_with_replacement(sorted(word),int(num)))

print(res1)
# [('A', 'C'), ('A', 'H'), ('A', 'K'), ('C', 'H'), ('C', 'K'), ('H', 'K')]

print(res2)
# [('A', 'A'), ('A', 'C'), ('A', 'H'), ('A', 'K'), ('C', 'C'), ('C', 'H'), ('C', 'K'), ('H', 'H'), ('H', 'K'), ('K', 'K')]

==================================================================================================================================================================

from itertools import groupby

num = input()
for key,group in groupby(num):
    print(key, len(list(group)))

#1111122223333444

1 5
2 4
3 4
4 3
