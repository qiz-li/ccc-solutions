"""
CCC '20 J4 - Cyclic Shifts
Find this problem at:
https://dmoj.ca/problem/ccc20j4
"""


def find_cycle_shifts(s):
    """
    Find all cycle shifts of a given string.

    Args:
        s: String to find cycle shifts.

    Returns:
        All cycle shifts of a given string.
    """
    s_lst = list(s)
    cycle_shifts = ['']
    while cycle_shifts[-1] != s:
        s_lst.insert(0, s_lst.pop())
        cycle_shifts.append(''.join(s_lst))
    return cycle_shifts[1:]


T = input()
if any(i in T for i in find_cycle_shifts(input())):
    print("yes")
else:
    print("no")
