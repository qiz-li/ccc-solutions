"""
CCC '05 J5 - Bananas
Find this problem at:
https://dmoj.ca/problem/ccc05j5
"""

match = {'B': {'S', 'A', 'B'}, 'N': {'B', 'A'},
         'A': {'N', 'S'}, 'S': {'N', 'S'}}


def solve(word):
    for char in word:
        if char in match[stack[-1]]:
            # Don't pop if letter is immediately after 'B' and not 'S'
            if not (stack[-1] == 'B' and char != 'S'):
                stack.pop()
                # 'S' does not match to any previous 'B'
                if char == 'S' and (not stack or stack.pop() != 'B'):
                    return False
            stack.append(char)
        else:
            return False
    return len(stack) == 1 and stack[-1] in {'A', 'S'}


word = input()
while word != 'X':
    stack = ['N']
    print("YES" if solve(word) else "NO")
    word = input()
