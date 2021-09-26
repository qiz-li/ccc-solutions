"""
CCC '18 J1 - Telemarketer or not?
Find this problem at:
https://dmoj.ca/problem/ccc18j1
"""

# First digit is 8 or 9
if (input() in ('8', '9')
    # Second & third digits are the same
    and input() == input()
        # Last digit is 8 or 9
        and input() in ('8', '9')):
    print("ignore")
# Not telemarketer
else:
    print("answer")
