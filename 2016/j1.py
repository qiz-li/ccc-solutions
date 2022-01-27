"""
CCC '16 J1 - Tournament Selection
Find this problem at:
https://dmoj.ca/problem/ccc16j1
"""

wins = 0
for _ in range(6):
    wins += 1 if input() == 'W' else 0

if wins < 1:
    print(-1)
elif wins < 3:
    print(3)
elif wins < 5:
    print(2)
else:
    print(1)
