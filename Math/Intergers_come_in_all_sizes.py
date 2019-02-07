Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is:  (c++ int) or  (C++ long long int).

As we know, the result of  grows really fast with increasing .

Let's do some calculations on very large integers.

Task 
Read four numbers a,b ,c ,d and , and print the result of a**b+c**d.

Input Format 
Integers a,b ,c ,d and  are given on four separate lines, respectively.

Constraints 
Output Format 
Print the result of  on one line.

# Enter your code here. Read input from STDIN. Print output to STDOUT

a, b , c, d = (int(input()) for _ in range(4))
result  = pow(a,b)+pow(c,d)
print (result)

