#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

s = [random.randint(0, 1000) for i in range(200)]


def bubble_sort(si):
    s = si[:]
    if len(s) == 1:
        return s
    n = 0
    while n < len(s):
        for i in range(len(s) - 1, n, -1):
            if s[i] < s[i - 1]:
                s[i], s[i - 1] = s[i - 1], s[i]
        n += 1
    return s


def main():
    print('Original s: \n' + str(s))
    s_sorted = bubble_sort(s)
    print('Sorted s: \n' + str(s_sorted))


if __name__ == "__main__":
    main()
