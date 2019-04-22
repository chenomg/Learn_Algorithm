#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import time
import logging
from functools import wraps


def run_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.clock()
        run = func(*args, **kwargs)
        end_time = time.clock()
        print('{name} costs time: {time} s'.format(
            name=func.__name__.upper(), time=str(end_time - start_time)))
        return run

    return wrapper


def check_order(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        s = func(*args, **kwargs)
        for i in range(1, len(s)):
            if s[i - 1] > s[i]:
                logging.warning('Order Wrong!!! --->  def: {}'.format(
                    func.__name__))
                return False
        return s

    return wrapper


@check_order
@run_time
def bubble_sort(s):
    if len(s) == 1:
        return s
    n = 0
    while n < len(s):
        for i in range(len(s) - 1, n, -1):
            if s[i] < s[i - 1]:
                s[i], s[i - 1] = s[i - 1], s[i]
        n += 1
    return s


@check_order
@run_time
def insertion_sort(s):
    lent = len(s)
    if lent == 1:
        return s
    for i in range(1, lent):
        k = i
        for j in range(i - 1, -1, -1):
            if s[i] < s[j]:
                k = j
            else:
                break
        t = s.pop(i)
        s.insert(k, t)
    return s


def main():
    s = [random.randint(0, 1000) for i in range(10000)]
    func_test = [bubble_sort, insertion_sort]
    ss = [s.copy() for i in range(len(func_test))]
    for func, s in zip(func_test, ss):
        func(s)


if __name__ == "__main__":
    main()
