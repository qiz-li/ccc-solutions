"""
CCC '00 S1 - Slot Machines
Find this problem at:
https://dmoj.ca/problem/ccc00s1
"""

quarters = int(input())
machines = [int(i) for i in [input(), input(), input()]]
pay_turn = [35, 100, 10]
pay = [30, 60, 9]
time = 0
while quarters > 0:
    # Find the machine to play at this turn
    turn = time % 3
    machines[turn] += 1
    # Machine reached pay turn!
    if machines[turn] == pay_turn[turn]:
        quarters += pay[turn]
        machines[turn] = 0
    quarters -= 1
    time += 1
print(f"Martha plays {time} times before going broke.")
