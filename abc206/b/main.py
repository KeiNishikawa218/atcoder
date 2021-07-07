#!/usr/bin/env python3

def main():
    n = int(input())

    for i in range(1, 10**5+1):
        if ((i**2) + i)/2 >= n:
            print(i)
            exit()
        


main()