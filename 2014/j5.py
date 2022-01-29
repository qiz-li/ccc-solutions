"""
CCC '14 J5/S2 - Assigning Partners
Find this problem at:
https://dmoj.ca/problem/ccc14s2
"""

n = int(input())
l1, l2 = input().split(), input().split()
partners = {}

for i in range(n):
    if l1[i] == l2[i]:
        print("bad")
        break
    elif l1[i] not in partners and l2[i] not in partners:
        partners[l1[i]] = l2[i]
        partners[l2[i]] = l1[i]
    elif partners.get(l1[i]) != l2[i] or partners.get(l2[i]) != l1[i]:
        print("bad")
        break
else:
    print("good")
