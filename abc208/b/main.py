#!/usr/bin/env python3

def main():
    p = int(input())

    ans = 0
    x = 2*3*4*5*6*7*8*9*10

    for i in range(10, 0, -1):
        if x <= p <= x*100:
            ans += p//x
            p = p%x
        
        x /= i

    print(int(ans))
main()