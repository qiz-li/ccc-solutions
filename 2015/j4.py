"""
CCC '15 J4 - Wait Time
Find this problem at:
https://dmoj.ca/problem/ccc15j4
"""

r_times = {}
received = set()
total_time = [0] * 101
time = 0

for _ in range(int(input())):
    cmd, id = input().split()
    id = int(id)
    if cmd == 'R':
        r_times[id] = time
        received.add(id)
    elif cmd == 'S':
        total_time[id] += time - r_times[id]
        received.remove(id)
    else:
        time += id - 2
    time += 1

for id, wait in enumerate(total_time):
    if wait != 0 or id in received:
        if id in received:
            print(id, -1)
        else:
            print(id, wait)
