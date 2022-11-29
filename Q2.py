"""
The included code stub will read an integer, n, from STDIN.

Without using any string methods, try to print the following:
123 ... n

Note that "..." represents the consecutive values in between.

EXAMPLE
n = 5
Print the string 12345.

INPUT FORMAT
The first line contains an integer n.

CONSTRAINTS
1 <= n <= 150

OUTPUT FORMAT
Print the list of integers from 1 through n as a string, without spaces.

SAMPLE INPUT 0
3

SAMPLE OUTPUT 0
123
"""

if __name__ == '__main__':
    n = int(input())
    
    
for i in range(1, n+1):
    print(i, end = '')
