"""
CCC '00 J1 - Calendar
Find this problem at:
https://dmoj.ca/problem/ccc00j1
"""

start, days = (int(i) for i in input().split())
# Start by padding until the day of the week on which the month begins
calender = ('   ,' * (start-1)).split(',')[:-1]
# Add the appropriate whitespace into each day
for i in range(1, days+1):
    calender.append(f'{str(i): >3}')
# Add the heading and split the calendar into weeks
full_calender = ([["Sun", "Mon", "Tue", "Wed", "Thr", "Fri", "Sat"]] +
                 [calender[i: i + 7] for i in range(0, len(calender), 7)])
# Print out the calendar
for week in full_calender:
    print(' '.join(week))
