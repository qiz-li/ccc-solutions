"""
CCC '15 J3 - Rövarspråket
Find this problem at:
https://dmoj.ca/problem/ccc15j3
"""

import string

vowels = {'a', 'e', 'i', 'o', 'u'}
alphabet = string.ascii_lowercase
word = list(input())

for idx in range(len(word)):
    if word[idx] not in vowels:
        i = j = alph_num = ord(word[idx]) - 97
        # Get closest vowel
        while True:
            i -= 1
            j += 1
            t = alphabet[i]
            if alphabet[i] in vowels:
                word[idx] += alphabet[i]
                break
            elif j < len(alphabet) and alphabet[j] in vowels:
                word[idx] += alphabet[j]
                break
        # Get next consonant
        if alph_num == len(alphabet) - 1:
            word[idx] += 'z'
        else:
            i = alph_num + 1
            while alphabet[i] in vowels:
                i += 1
            word[idx] += alphabet[i]

print(''.join(word))
