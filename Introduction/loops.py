# Task 
#Read an integer . For all non-negative integers , print . See the sample for details.

# Input Format

# The first and only line contains the integer, .

# Constraints
1 <= N <= 20 

# Output Format

# Print N lines, one corresponding to each .


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        i = i**2
        print (i)
