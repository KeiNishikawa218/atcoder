#!/usr/bin/env python3

def main():
    ll = list(map(int, input().split())) 
    ll.sort(reverse = True)

    print(ll[0]+ll[1])


main()