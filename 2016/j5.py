"""
CCC '16 J5/S2 - Tandem Bicycle
Find this problem at:
https://dmoj.ca/problem/ccc16s2
"""

question_num = int(input())
n = int(input())

dmojistan = list(map(int, input().split()))
pegland = list(map(int, input().split()))

dmojistan.sort()
pegland.sort()

if question_num == 1:
    min_sum = 0
    for i in range(n):
        min_sum += max(dmojistan[i], pegland[i])
    print(min_sum)
else:
    max_sum = 0
    for i in range(n):
        max_sum += max(dmojistan[i], pegland[len(pegland) - i - 1])
    print(max_sum)
