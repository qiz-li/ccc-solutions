"""
CCC '14 J2 - Vote Count
Find this problem at:
https://dmoj.ca/problem/ccc14j2
"""

_, vote = input(), input()
a, b = vote.count('A'), vote.count("B")
if a > b:
    print("A")
elif b > a:
    print("B")
else:
    print("Tie")
