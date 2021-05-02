#!/usr/bin/env python3


from collections import deque

d = deque()
rev = False

for s in input():
    if s == 'R':
        rev = not rev
    elif rev:
        if d and d[0] == s:
            d.popleft()
        else:
            d.appendleft(s)
    else: 
        if d and s == d[-1]:
            d.pop()
        else:
            d.append(s)

if rev:
    d = reversed(d)

print(''.join(d))
