#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import time
import logging
from functools import wraps

import pysnooper
from numba import jit, njit


def run_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.process_time()
        run = func(*args, **kwargs)
        end_time = time.process_time()
        print(
            '{name} costs time:'.format(name=func.__name__.upper()).rjust(
                30, '-'),
            str(end_time - start_time) + 's')
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


# @pysnooper.snoop('results_bubble_sort.txt')
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


# @pysnooper.snoop('results_bubble_sort.txt')
@check_order
@run_time
@jit
def bubble_sort_jit(s):
    if len(s) == 1:
        return s
    n = 0
    while n < len(s):
        for i in range(len(s) - 1, n, -1):
            if s[i] < s[i - 1]:
                s[i], s[i - 1] = s[i - 1], s[i]
        n += 1
    return s


# @pysnooper.snoop('results_insertion_sort.txt')
@check_order
@run_time
@jit
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


# @pysnooper.snoop('results_merge_sort.txt')
@check_order
@run_time
def merge_sort(s):
    def _merge_sort(s):
        def _split_to_two(sp):
            mid = len(sp) // 2
            return sp[:mid], sp[mid:]

        def _merge_two(sp1, sp2):
            index_1 = 0
            index_2 = 0
            s_m = []
            while index_1 < len(sp1) and index_2 < len(sp2):
                if sp1[index_1] < sp2[index_2]:
                    s_m.append(sp1[index_1])
                    index_1 += 1
                else:
                    s_m.append(sp2[index_2])
                    index_2 += 1
            if index_1 == len(sp1):
                s_m += sp2[index_2:]
            else:
                s_m += sp1[index_1:]
            return s_m

        if len(s) == 1:
            return s
        if len(s) > 1:
            sp1, sp2 = _split_to_two(s)
            return _merge_two(_merge_sort(sp1), _merge_sort(sp2))

    return _merge_sort(s)


# @pysnooper.snoop('results_merge_sort.txt')
@check_order
@run_time
def quick_sort(s):
    def _quick_sort(s):
        def _split_to_two(sp):
            mid = len(sp) // 2
            return sp[:mid], sp[mid:]

        def _merge_two(sp1, sp2):
            index_1 = 0
            index_2 = 0
            s_m = []
            while index_1 < len(sp1) and index_2 < len(sp2):
                if sp1[index_1] < sp2[index_2]:
                    s_m.append(sp1[index_1])
                    index_1 += 1
                else:
                    s_m.append(sp2[index_2])
                    index_2 += 1
            if index_1 == len(sp1):
                s_m += sp2[index_2:]
            else:
                s_m += sp1[index_1:]
            return s_m

        if len(s) == 1:
            return s
        if len(s) > 1:
            sp1, sp2 = _split_to_two(s)
            return _merge_two(_merge_sort(sp1), _merge_sort(sp2))

    return _quick_sort(s)


def main():
    s = [random.randint(0, 1000) for i in range(50000)]
    func_test = [bubble_sort_jit, insertion_sort, merge_sort]
    ss = [s.copy() for i in range(len(func_test))]
    for func, s in zip(func_test, ss):
        func(s)
    input('Press Enter to Exit!')


if __name__ == "__main__":
    main()
