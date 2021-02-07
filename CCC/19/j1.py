# CCC '19 J1 - Winning Score
# Find this problem at:
# https://dmoj.ca/problem/ccc19j1

# Sum of points for both teams
a_points = sum([(3-time)*int(input()) for time in range(3)])
b_points = sum([(3-time)*int(input()) for time in range(3)])

# Determine the game result
if a_points > b_points:
    print("A")
elif b_points > a_points:
    print("B")
else:
    print("T")
