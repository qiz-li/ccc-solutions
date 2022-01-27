"""
CCC '16 J4 - Arrival Time
Find this problem at:
https://dmoj.ca/problem/ccc16j4
"""

# NOTE: It seems like I overcomplicated this problem.
# A much simpler solution can be achieved
# by simply keeping tack of the distance and time

hour, minute = map(int, input().split(':'))


def print_time(hour, minute):
    if minute >= 60:
        hour += minute // 60
        minute = minute % 60
    if hour >= 24:
        hour = hour % 24
    print(f"{str(hour).zfill(2)}:{str(minute).zfill(2)}")


# Departs during traffic
if 7 <= hour < 10 or 15 <= hour < 19:
    # Check if morning or afternoon traffic
    traffic_end = 10 if hour < 10 else 19
    # Time in traffic
    travel_time = ((traffic_end - (hour + 1)) * 60 + (60 - minute))
    # Time outside traffic
    travel_time += 120 - (travel_time // 2)

# Encounters traffic
elif 7 <= hour + 2 < 10 or 15 <= hour + 2 < 19:
    # Check if morning or afternoon traffic
    traffic_start = 7 if hour < 10 else 15
    # Time outside traffic
    travel_time = (traffic_start - (hour + 1)) * 60 + (60 - minute)
    # Goes through entirety of traffic and has more to go (e.g. 06:40)
    if traffic_start == 7 and travel_time + 90 < 120:
        travel_time += 180 + 120 - (travel_time + 90)
    else:
        # Time in traffic
        travel_time += (120 - travel_time) * 2

# Does not encounter traffic
else:
    travel_time = 120

print_time(hour, minute + travel_time)
