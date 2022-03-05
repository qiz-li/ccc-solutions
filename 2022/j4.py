"""
CCC '22 S2 - Good Groups
Find this problem at:
https://dmoj.ca/problem/ccc22s2
"""

must, must_not = {}, {}
# Only one of the students is added as key into the rules dictionary.
# This will avoid duplicates when checking the groups.
for rules in (must, must_not):
    for _ in range(int(input())):
        s1, s2 = input().split()
        if s1 not in rules:
            rules[s1] = [s2]
        else:
            rules[s1].append(s2)

violations = 0
for _ in range(int(input())):
    group = set(input().split())
    for i in group:
        # If student in must list is not in group, add a violation.
        # If student in must not list is in group, also add a violation.
        violations += sum(1 for mi in must.get(i, []) if mi not in group) + \
            sum(1 for mni in must_not.get(i, []) if mni in group)

print(violations)
