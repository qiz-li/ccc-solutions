"""
CCC '13 J2 - Rotating letters
Find this problem at:
https://dmoj.ca/problem/ccc13j2
"""

print("YES" if all(i in {'I', 'O', 'S', 'H', 'Z', 'X', 'N'}
                   for i in input()) else "NO")
