"""
CCC '18 J5 - Choose your own path
Find this problem at:
https://dmoj.ca/problem/ccc18j5
"""

from queue import Queue
book = {}

# Construct book with all pages
for page in range(int(input())):
    num_paths, *destinations = input().split()
    if int(num_paths) == 0:
        book[page + 1] = [0]
    else:
        book[page + 1] = [int(i) for i in destinations]

# We are going to use breadth-first-search to find all paths
q = Queue()
q.put([1])
reached = {1}
valid = []
while q.qsize() > 0:
    path = q.get()
    for page in book[path[-1]]:
        if page == 0:
            valid.append(path)
        elif page not in reached:
            reached.add(page)
            q.put(path + [page])

if len(reached) == len(book):
    print("Y")
else:
    print("N")
print(len(valid[0]))
