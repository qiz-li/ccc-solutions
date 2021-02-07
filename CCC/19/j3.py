# CCC '19 J3 - Cold Compress
# Find this problem at:
# https://dmoj.ca/problem/ccc19j3

# !NOTE! The following passed on DMOJ but failed the second test case
# on the official CCC grader. I do not know why.

lines = int(input())
for _ in range(lines):
    last_char = ""
    output = ""
    count = 0
    for char in input():
        # Character changed, reset counter and record results
        if char != last_char:
            if last_char:
                output += f"{count} {last_char} "
            count = 1
            last_char = char
        # Character is the same, add to counter
        elif char == last_char:
            count += 1
    output += f"{count} {last_char} "
    print(output.strip())
