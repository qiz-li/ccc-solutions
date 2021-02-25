"""
CCC '17 J3 - Exactly Electrical
Find this problem at:
https://dmoj.ca/problem/ccc17j3
"""

start_x, start_y = (int(i) for i in input().split())
end_x, end_y = (int(i) for i in input().split())
electricity = int(input())
distance = abs(start_x - end_x) + abs(start_y - end_y)

# If the distance is a even number, the electricity has to
# be greater or equal to the distance and also be even.
# Same if the distance is odd, the electricity also has to be odd.
# This is to the nature that every action is followed by an anti-action
# that will eventually be a multiple of two. If you go up and back down,
# it takes two electricity. If you go in a circle, it takes four.
# If you go in two circles, it takes eight...
if electricity >= distance and (distance % 2 == 0 and electricity % 2 == 0 or
                                distance % 2 != 0 and electricity % 2 != 0):
    print('Y')
else:
    print('N')
