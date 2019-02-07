ABC is a right triangle, 90 at B.
Therefore, ABC =90 .

PointM  is the midpoint of hypotenuse AC.

You are given the lengths AB and BC. 
Your task is to find MBC (angle , as shown in the figure) in degrees.

Input Format

The first line contains the length of side .
The second line contains the length of side .

Constraints


Lengths  and  are natural numbers.
Output Format

Output  in degrees. 

Note: Round the angle to the nearest integer.

Examples: 
If angle is 56.5000001°, then output 57°. 
If angle is 56.5000000°, then output 57°. 
If angle is 56.4999999°, then output 56°.


Sample Input

10
10
Sample Output

45°

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB = int(input())
BC = int(input())
# Math.atan2() function returns the angle in the plane (in radians) 
radians = math.atan2(AB, BC)
# Convert radians to degree
deg = math.degrees(radians)
# Convert deg to int and then to str to add the ˚ symbol
print (str(int(deg))+ '°')


#https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan2
