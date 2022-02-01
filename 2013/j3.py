"""
CCC '13 J3/S1 - From 1987 to 2013
Find this problem at:
https://dmoj.ca/problem/ccc13s1
"""

year = int(input()) + 1
while len(set(str(year))) != len(str(year)):
    year += 1
print(year)
