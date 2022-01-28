"""
CCC '15 J1 - Special Day
Find this problem at:
https://dmoj.ca/problem/ccc15j1
"""

month, day = int(input()), int(input())

if month > 2 or (month == 2 and day > 18):
    print("After")
elif month < 2 or (month == 2 and day < 18):
    print("Before")
else:
    print("Special")
