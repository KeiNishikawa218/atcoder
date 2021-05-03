#!/usr/bin/env python3

def main():
    from collections import deque
    a = deque(list(input()))
    b = deque(list(input()))
    c = deque(list(input()))

    a.append('')
    b.append('')
    c.append('')    

    turn = 'a'

    ans = ''
    while a and b and c:
        ans = turn
        if turn == 'a':
            turn = a.popleft()
        elif turn == 'b':
            turn = b.popleft()
        else:
            turn = c.popleft()

    print(ans.upper())
main()