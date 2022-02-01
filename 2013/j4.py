"""
CCC '13 J4 - Time on task
Find this problem at:
https://dmoj.ca/problem/ccc13j4
"""

mins, n = int(input()), int(input())
tasks = [int(input()) for _ in range(n)]
tasks.sort()

t_nums = t_mins = 0
for i in tasks:
    t_mins += i
    if t_mins > mins:
        break
    t_nums += 1
print(t_nums)
