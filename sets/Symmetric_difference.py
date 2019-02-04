# Symmetric Difference

# Objective 
# Today, we're learning about a new data type: sets.

# Concept
# If the inputs are given on one line separated by a space character, use split() to get the separate values in the form of a list:
# >> a = raw_input()
# 5 4 3 2
# >> lis = a.split()
# >> print (lis)
# ['5', '4', '3', '2']

# If the list values are all integer types, use the map() method to convert all the strings to integers.
# >> newlis = list(map(int, lis))
# >> print (newlis)
# [5, 4, 3, 2]

# Sets are an unordered bag of unique values. A single set contains values of any immutable data type. 

# Task 
# Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those
# values that exist in either M or N but do not exist in both.

# Input Format
# The first line of input contains an integer, M. 
# The second line contains M space-separated integers. 
# The third line contains an integer, N. 
# The fourth line contains N space-separated integers.

# Output Format
# Output the symmetric difference integers in ascending order, one per line.


# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    a_len = int(input())
    a_set = set(map(int,input().split()))
    b_len = int(input())
    b_set = set(map(int,input().split()))

    result1 = a_set.difference(b_set)
    result2 = b_set.difference(a_set)

    f_result = result1.union(result2)

    s_result = sorted(f_result)

    for element in s_result:
        print (element)
