from collections import Counter

myList = [1,2,2,2,3,3,3,3,4,4,4,4,4,4,4,4,4,4]
print(Counter((myList)))
print (Counter(myList).items())
print (Counter(myList).keys())
print (Counter(myList).values())

# Output
# Counter({4: 10, 3: 4, 2: 3, 1: 1})
# dict_items([(1, 1), (2, 3), (3, 4), (4, 10)])
# dict_keys([1, 2, 3, 4])
# dict_values([1, 3, 4, 10])


==================================================================================================================================
