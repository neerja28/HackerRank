Task

You are given a date. Your task is to find what the day is on that date.

Input Format

A single line of input containing the space separated month, day and year, respectively, in    format.

Constraints

Output Format

Output the correct day in capital letters.

Sample Input

08 05 2015
Sample Output

WEDNESDAY
Explanation

The day on August 5th was WEDNESDAY.

# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

month, day, year = map(int,input().split())
num = calendar.day_name[calendar.weekday(year,month,day)]
print (num.upper())

#Mon =0, Tue=1 and so on..
