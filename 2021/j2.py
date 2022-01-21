"""
CCC '21 J2 - Silent Auction
Find this problem at:
https://dmoj.ca/problem/ccc21j2
"""

max_price = -1
for _ in range(int(input())):
    person, price = input(), int(input())
    if price > max_price:
        max_price, max_person = price, person

print(max_person)
