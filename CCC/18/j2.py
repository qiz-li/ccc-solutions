"""
CCC '18 J2 - Occupy parking
Find this problem at:
https://dmoj.ca/problem/ccc18j2
"""

input()
count = 0
# Combine yesterday's spot value with today's value
for yday, tday in zip(list(input()), list(input())):
    # Add to count if the spot was occupied both days
    if yday == tday == 'C':
        count += 1
print(count)
