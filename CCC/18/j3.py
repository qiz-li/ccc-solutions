"""
CCC '18 J3 - Are we there yet?
Find this problem at:
https://dmoj.ca/problem/ccc18j3
"""

distances = [int(i) for i in input().split()]
for i in range(5):
    val = 0
    output = []
    # Find the distances before given city
    for distance in distances[:i][::-1]:
        val += distance
        output.append(val)
    output.reverse()
    val = 0
    # Find the distances after given city
    for distance in distances[i:]:
        val += distance
        output.append(val)
    output.insert(i, 0)
    print(' '.join(str(i) for i in output))
