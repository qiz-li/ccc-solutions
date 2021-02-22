"""
CCC '17 J4 - Favourite Times
Find this problem at:
https://dmoj.ca/problem/ccc17j4
"""

duration = int(input())
days = count = 0

# Find how many full twelve-hours is in
# the duration and calculate what remains
if duration >= 720:
    days = duration // 720
    duration = duration % 720

hour, minutes = 12, 1

for i in range(duration):
    clock = [int(i) for i in str(hour) + str(minutes)]

    # Pad zero to minutes if needed
    if len(str(minutes)) == 1:
        clock.insert(-1, 0)

    # Check if it is arithmetic sequence
    dif = clock[1] - clock[0]
    if all(clock[idx + 1] - clock[idx] == dif
           for idx in range(len(clock) - 1)):
        count += 1

    minutes += 1
    if minutes == 60:
        hour += 1
        minutes = 0
    if hour == 13:
        hour = 1

# The thirty one comes from the amount of "favourtie times" during a full
# twelve hours. This is found by first running the above sequence with
# a duration of 720 (12 * 60) minutes.
# favorite_times = [1234, 111, 123, 135, 147, 159, 210, 222, 234, 246, 258,
#                   321, 333, 345, 357, 420, 432, 444, 456, 531, 543, 555, 630,
#                   642, 654, 741, 753, 840, 852, 951, 1111]
print(days * 31 + count)
