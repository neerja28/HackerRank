You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
Input Format

A single line containing a string .

Constraints


Output Format

Print the modified string .

Sample Input 0

HackerRank.com presents "Pythonist 2".
Sample Output 0

hACKERrANK.COM PRESENTS "pYTHONIST 2".


# Enter your code here 
def swap_case(s):
    res = ""
    for letter in s:
        if letter.isupper() == True:
            res = res + letter.lower()
        else:
            res = res + letter.upper()
    return res


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
# Easy method 

def swap_case(s):
    return (s.swapcase())

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
