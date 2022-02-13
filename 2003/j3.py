"""
CCC '03 J3/S1 - Snakes and Ladders
Find this problem at:
https://dmoj.ca/problem/ccc03s1
"""

connections = {54: 19, 90: 48, 99: 77, 9: 34, 40: 64, 67: 86}
cur = 1

while True:
    move = int(input())
    if move == 0:
        print("You Quit!")
        break
    cur += move
    if cur > 100:
        cur -= move
    elif cur in connections:
        cur = connections[cur]
    print(f"You are now on square {cur}")
    if cur == 100:
        print("You Win!")
        break
