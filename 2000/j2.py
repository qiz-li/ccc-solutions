"""
CCC '00 J2 - 9966
Find this problem at:
https://dmoj.ca/problem/ccc00j2
"""

valid = 0
# Loop through the given interval
for number in range(int(input()), int(input()) + 1):
    # Reverse the number and replace 6 with 9 and 9 with 6
    # to get the flipped number
    if (all(i in ('0', '1', '6', '8', '9') for i in str(number))
       and number == int(str(number).replace('9', 'x').replace('6', '9').
       replace('x', '6')[::-1])):
        valid += 1
print(valid)
