"""
CCC '21 J4 - Arranging Books
Find this problem at:
https://dmoj.ca/problem/ccc21j4
"""

books = input()

l_end = books.count('L')
m_end = l_end + books.count('M')

l_sec, m_sec, s_sec = books[:l_end], books[l_end:m_end], books[m_end:]

print(l_sec.count('M') + l_sec.count('S') +
      max(m_sec.count('S'), s_sec.count('M')))
