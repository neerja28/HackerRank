# Finding the percentage

# You have a record of N students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The
# marks can be floating values. The user enters some integer N followed by the names and marks for N students. You are required to save
# the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that
# student, correct to two decimal places.

# Input Format
# The first line contains the integer N, the number of students. The next N lines contains the name and marks obtained by that student
# separated by a space. The final line contains the name of a particular student previously listed.

# Constraints
# 2 <= N <= 10
# 0 <= Marks <= 100

# Output Format
# Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.


# Enter your code here. Read input from STDIN. Print output to STDOUT

d = dict()
l = list()
n = int(input())

for i in range(0,n):
    name_and_marks = input()
    l = name_and_marks.split(" ")
    key = l[0]
    d[key] = float((float(l[1])+float(l[2])+float(l[3]))/3)
search_name = input()
print ("{0:.2f}".format(d[search_name]))
