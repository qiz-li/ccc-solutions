"""
CCC '03 J4/S2 - Poetry
Find this problem at:
https://dmoj.ca/problem/ccc03s2
"""

vowels = {'a', 'e', 'i', 'o', 'u'}
for _ in range(int(input())):
    verses = []
    for _ in range(4):
        word = input().split()[-1]
        for idx in range(len(word) - 1, -1, -1):
            if word[idx].lower() in vowels:
                syllable = word[idx:]
                break
        else:
            syllable = word
        verses.append(''.join(i.lower() for i in syllable))

    if all(i == verses[0] for i in verses):
        print('perfect')
    elif verses[0] == verses[1] and verses[2] == verses[3]:
        print('even')
    elif verses[0] == verses[2] and verses[1] == verses[3]:
        print('cross')
    elif verses[0] == verses[3] and verses[1] == verses[2]:
        print('shell')
    else:
        print('free')
