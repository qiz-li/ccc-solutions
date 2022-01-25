"""
CCC '19 J5 - Rule of Three
Find this problem at:
https://dmoj.ca/problem/ccc19j5
"""

# NOTE! This works on the official CCC test cases,
# but unfortunately is not fast enough for the full DMOJ test cases.

import sys
from functools import lru_cache
from collections import defaultdict

rules = defaultdict(list)
lengths = defaultdict(list)
visited = set()

for i in range(3):
    f, t = sys.stdin.readline().split()
    rules[f].append((i + 1, t))
    lengths[len(f)].append(f)

target_steps, start, target = sys.stdin.readline().split()
target_steps = int(target_steps)


@lru_cache
def get_convertions(cur):
    convertions = []
    for length, changes in lengths.items():
        for idx in range(len(cur) - length + 1):
            for change in changes:
                if cur[idx:idx + length] == change:
                    for rule_num, new in rules[change]:
                        convertions.append(
                            (rule_num, idx + 1,
                             cur[:idx] + new + cur[idx + length:]))
    return convertions


def convert(prev, step):
    cur = prev[-1][-1]
    if step == target_steps and cur == target:
        for operation in prev[1:]:
            print(*operation)
        return True
    elif step >= target_steps or cur + str(step) in visited:
        return False
    else:
        visited.add(cur + str(step))
        for changed in get_convertions(cur):
            if convert(prev + [changed], step + 1):
                return True


convert([(0, 0, start)], 0)
