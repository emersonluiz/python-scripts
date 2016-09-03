#!/usr/bin/env python

def fibonacci(previous, current, n):
    r = (previous + current)
    print str(n) + " : " + str(r)
    n += 1

    if n <= 20:
        fibonacci(current, r, n)

fibonacci(0, 1, 1)