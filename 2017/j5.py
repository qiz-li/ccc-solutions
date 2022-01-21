"""
CCC '17 J5/S3 - Nailed It!
Find this problem at:
https://dmoj.ca/problem/ccc17s3
"""

input()
lengths = [0] * 2001
for length in map(int, input().split()):
    lengths[length] += 1

length_sums = [0] * 4002
for len1 in range(0, len(lengths)):
    num1 = lengths[len1]
    if num1 > 0:
        for len2 in range(len1, len(lengths)):
            if len1 == len2:
                length_sums[len1 + len2] += num1 // 2
            else:
                num2 = lengths[len2]
                length_sums[len1 + len2] += min(num1, num2)

max_num = different = 0
for num in length_sums:
    if num > max_num:
        max_num = num
        different = 1
    elif num == max_num:
        different += 1

print(max_num, different)
