"""
CCC '20 J2 - Epidemiology
Find this problem at:
https://dmoj.ca/problem/ccc20j2
"""

limit = int(input())
new = people = int(input())
increment = int(input())
day = 1
while people <= limit:
    # The amount of infections grow in a geometric sequence
    people += new * increment ** day
    day += 1
print(day-1)
