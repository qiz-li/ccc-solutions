# CCC '19 J2 - Time to Decompress
# Find this problem at:
# https://dmoj.ca/problem/ccc19j2

for _ in range(int(input())):
    # Unpack the input into integer and symbol
    integer, symbol = input().split()
    # Time the symbol by integer amount of times
    print(int(integer) * symbol)
