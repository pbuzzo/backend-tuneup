#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "Patrick Buzzo"

import cProfile
import pstats
import functools
import timeit
import re


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    def inner_function(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        final = func(*args, **kwargs)
        pr.disable()
        pstats.Stats(pr).sort_stats('cumulative').print_stats()
        return final
    return inner_function


# @profile
def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read()



@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    doubles = []
    singles = []
    name_list = re.findall(r'[A-Z]+.*[a-z]+', movies)
    for name in name_list:
        if name.lower() in singles:
            doubles.append(name)
        else:
            singles.append(name.lower())
    return doubles


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    t = timeit.Timer(stmt='find_duplicate_movies("movies.txt")')
    result = t.repeat(repeat=7, number=3)
    avg_list = []
    for clock in result:
        avg_list.append(clock/3)
    average = min(avg_list)
    print('Best time across 5 repeats of 3 runs per repeat:{} sec'.format(average))


def main():
    """Computes a list of duplicate movie entries"""
    # timeit_helper()
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))


if __name__ == '__main__':
    main()
