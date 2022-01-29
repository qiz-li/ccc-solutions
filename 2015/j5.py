"""
CCC '15 J5 - π-day
Find this problem at:
https://dmoj.ca/problem/ccc15j5
"""

n, k = int(input()), int(input())
memorize = {}


def pie(n, k, start):
    if (n, k, start) not in memorize:
        if k == 1:
            memorize[(n, k, start)] = 1
        else:
            total = 0
            for i in range(start, n//k + 1):
                total += pie(n - i, k - 1, i)
            memorize[(n, k, start)] = total
    return memorize[(n, k, start)]


print(pie(n, k, 1))
