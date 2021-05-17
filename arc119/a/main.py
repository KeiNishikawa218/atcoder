#!/usr/bin/env python3

def main():
    n = int(input())

    ans =  n
    #60
    for b in range(1, 60):
        ans = min(ans, b + n//2**b + n%2**b)
    
    print(ans)


main()