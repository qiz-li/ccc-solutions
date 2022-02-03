"""
CCC '12 J2 - Sounds fishy!
Find this problem at:
https://dmoj.ca/problem/ccc12j2
"""

nums = [int(input()) for _ in range(4)]

if all(nums[i] < nums[i + 1] for i in range(len(nums) - 1)):
    print("Fish Rising")
elif all(nums[i] > nums[i + 1] for i in range(len(nums) - 1)):
    print("Fish Diving")
elif all(nums[i] == nums[i + 1] for i in range(len(nums) - 1)):
    print("Fish At Constant Depth")
else:
    print("No Fish")
