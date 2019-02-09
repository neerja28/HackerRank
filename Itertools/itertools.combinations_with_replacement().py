# itertools.combinations_with_replacement(iterable, r) 
# This tool returns  length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.
# Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in
# sorted order.

# Task
# You are given a string S. 
# Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.

# Input Format
# A single line containing the string S and integer value k separated by a space.

# Constraints
# 0 < k <= len(S)
# The string contains only UPPERCASE characters.

# Output Format
# Print the combinations with their replacements of string S on separate lines.


# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement
word, num = input().split()
res2 = list(combinations_with_replacement(sorted(word),int(num)))
for i in res2:
    print ("".join(i))
