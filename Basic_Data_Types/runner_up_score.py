# Find the Second Largest Number

# You are given N numbers. Store them in a list and find the second largest number.

# Input Format 
# The first line contains N. The second line contains an array A[] of N integers each separated by a space.

# Constraints
# 2 <= N <= 10
# -100 <= A[i] <= 100

# Output Format 
# Output the value of the second largest number.


# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    n = int(input())
    map_arr = map(int, input().split())
    set_arr = set(map_arr)
    list_arr = sorted(list(set_arr))
    print (list_arr[-2])

    
    # Python map syntax
    
    map(fun,iter)
    
    
    Create a map object
    convert map object to set 
    convert set to list and proceed with list operations
    
    Map --> set ---> list (+operations)
