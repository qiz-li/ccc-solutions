"""
CCC '16 J3 - Hidden Palindrome
Find this problem at:
https://dmoj.ca/problem/ccc16j3
"""


def is_palindrome(word):
    # Easier way probably would have been to
    # just resverse the word and check if it is the same.
    # However, this is slightly more efficient.
    for i in range(len(word)):
        if len(word) == 1:
            return True
        j = len(word) - 1 - i
        while i < j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        return True


word = input()
max_len = 0
for i in range(len(word)):
    for j in range(1, len(word) + 1):
        bruh = word[i:j]
        if is_palindrome(bruh) and len(bruh) > max_len:
            max_len = len(bruh)

print(max_len)
