#!/usr/bin/env python3

def main():
    a, b = map(int, input().split())

    print(max(b-a+1, 0))


main()