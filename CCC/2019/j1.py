"""
CCC '19 J1 - Winning Score
Find this problem at:
https://dmoj.ca/problem/ccc19j1
"""

# Sum of points for both teams
a, b = (sum((3-time)*int(input()) for time in range(3)) for i in range(2))

# Determine the game result
if a > b:
    print("A")
elif b > a:
    print("B")
else:
    print("T")
