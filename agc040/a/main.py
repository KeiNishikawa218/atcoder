#!/usr/bin/env python3

def main():
    s = input()
    s = '>>><'
    n = len(s)

    i = 0
    ans = 0

    while i < n:
        cntL = 1
        cntR = 1

        if s[i] == '>':
            while i < n-1:
                cntL += 1
                if s[i+1] == '<':
                    break
                i += 1
        
            ans += cntL*(cntL+1)//2
        else:
            while i < n-1:
                if s[i] == '>':
                    cntL += 1
                else:
                    cntR += 1
                
                if s[i] == '>' and s[i+1] == '<':
                    break

                i += 1
        
            print(f'{cntL} {cntR}')
            mx = max(cntL, cntR)
            mm = min(cntL, cntR)-1
 
            ans += mx*(mx+1)//2 + mm*(mm+1)//2
        i += 1
        print(i)
    print(ans)

main()