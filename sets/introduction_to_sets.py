# Introduction to Sets

# A set is an unordered collection of elements without duplicate entries. 
# When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

# Basically, sets are used for membership testing and eliminating duplicate entries. 

# Task
# Now, let's use our knowledge of sets and help Mickey.
# Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the
# plants with distinct heights in her greenhouse.

# Formula used:
# Average = Sum of Distinct Heights / Total Number of Distinct Heights

# Input Format
# The first line contains the integer, N, the total number of plants.
# The second line contains the N space separated heights of the plants.

# Constraints
# 0 < N <= 100

# Output Format
# Output the average height value on a single line.


# Enter your code here. Read input from STDIN. Print output to STDOUT

def average(array):
    # your code goes here
    sum  = 0
    # Converting the array to set to remove duplicates 
    s_arr = set(array)
    for num in s_arr:
        sum += num 
    len_arr = len(s_arr)
    result = sum/len_arr
    return result


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
