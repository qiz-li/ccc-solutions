"""
CCC '12 J1 - Speed fines are not fine!
Find this problem at:
https://dmoj.ca/problem/ccc12j1
"""

diff = -int(input()) + int(input())

if diff >= 31:
    print("You are speeding and your fine is $500.")
elif diff >= 21:
    print("You are speeding and your fine is $270.")
elif diff >= 1:
    print("You are speeding and your fine is $100.")
else:
    print("Congratulations, you are within the speed limit!")
