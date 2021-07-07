#!/usr/bin/env python3
import math

def main():
    a, b, c = map(int, input().split())
        
    if c%2 == 1:
        if a < 0 and b > 0:
            print('<')
        elif a > 0 and b < 0:
            print('>')
        else:
            if a == 0 and b == 0:
                print('=')
                exit()

            if a == 0:
                if b > 0:
                    print('<')
                else:
                    print('>')
                exit()
            if b == 0:
                if a > 0:
                    print('>')
                else:
                    print('<')
                exit()

            a, b = abs(a), abs(b)

            if a == b:
                print('=')
                exit()

            if c * math.log(a) - c * math.log(b) > 0:
                print('>')
            else:
                print('<') 
    else:
        if a == 0 and b == 0:
            print('=')
            exit()
        
        if a == 0:
            print('<')
            exit()
        if b == 0:
            print('>')
            exit()

        a, b = abs(a), abs(b)

        if a == b:
            print('=')
            exit()

        if c * math.log(a) - c * math.log(b) > 0:
            print('>')
        else:
            print('<')

main()