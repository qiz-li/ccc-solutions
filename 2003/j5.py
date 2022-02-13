"""
CCC '03 J5/S3 - Floor Plan
Find this problem at:
https://dmoj.ca/problem/ccc03s3
"""

wood, r, c = int(input()), int(input()), int(input())
house = []
for _ in range(r):
    house.append([i for i in input()])

visited = set()
rooms = []
for x in range(r):
    for y in range(c):
        # BFS to find all rooms
        if house[x][y] == '.' and (x, y) not in visited:
            q = [(x, y)]
            visited.add((x, y))
            count = 1
            while q:
                cx, cy = q.pop(0)
                for dx, dy in [(cx + 1, cy), (cx - 1, cy),
                               (cx, cy + 1), (cx, cy - 1)]:
                    if (house[dx][dy] == '.' and
                        (dx, dy) not in visited and
                            0 <= dx < r and 0 <= dy < c):
                        visited.add((dx, dy))
                        q.append((dx, dy))
                        count += 1
            rooms.append(count)

total = rm_num = 0
if rooms:
    for rm_num, room in enumerate(sorted(rooms)[::-1]):
        total += room
        if total > wood:
            total -= room
            break
    else:
        rm_num += 1
print(f"{rm_num} room{'s' if rm_num > 1 or rm_num == 0 else ''},"
      f" {wood - total} square metre(s) left over")
