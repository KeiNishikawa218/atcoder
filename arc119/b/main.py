#!/usr/bin/env python3

def main():
    from collections import deque
    n = int(input())
    s = input()
    t = input()

    s_dash = s[::-1]
    t_dash = t[::-1]

    ans = 0
    ans_dash = 0

    sq = deque()
    tq = deque()

    sq_dash = deque()
    tq_dash = deque()

    for i in range(n):
        if s[i] == '0':
            sq.append(i)
        if t[i] == '0':
            tq.append(i)

        if s_dash[i] == '0':
            sq_dash.append(i)
        if t_dash[i] == '0':
            tq_dash.append(i)

    if len(sq) != len(tq):
        print(-1)
        exit()
    
    for i in range(len(sq)):
        a, b = sq.popleft(), tq.popleft()
        c, d = sq_dash.popleft(), tq_dash.popleft()

        if a > b:
            ans += 1
        elif b > a:
            if len(sq) > 1:
                if sq[0] >= b:
                    ans += 1
                else:
                    ans += b - a
            else:
                ans += b - a

        if c > d:
            ans_dash += 1
        elif d > c:
            # ans_dash += d - c
            if len(sq_dash) > 1:
                if sq_dash[0] >= d:
                    ans_dash += 1
                else:
                    ans_dash += d - c
            else:
                ans_dash += d - c

        # print(f'{ans} {ans_dash}')

    print(min(ans, ans_dash))

main()