"""
CCC '00 S2 - Babbling Brooks
Find this problem at:
https://dmoj.ca/problem/ccc00s2
"""

# Initial number and flow of streams on the top of the mountain
init_streams = int(input())
streams = [int(input()) for i in range(init_streams)]
while True:
    line = int(input())
    # We have reached the bottom!
    if line == 77:
        break
    # Combining the value of two streams into one
    elif line == 88:
        num_stream = int(input())
        streams[num_stream-1] += streams.pop(num_stream)
    # Separating the value of stream index n-1
    # into stream index n-1 and stream index n
    elif line == 99:
        num_stream, percent = (int(input()), int(input()))
        cur_val = streams.pop(num_stream-1)
        streams.insert(num_stream-1, cur_val*percent/100)
        streams.insert(num_stream, cur_val*(100-percent)/100)
# Round and print out the value of all streams at the bottom
print(' '.join(str(int(i)) for i in streams))
