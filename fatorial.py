#!/usr/bin/env python

def fatorial(n):
    if n<=1:
        return 1
    else:
        return n*fatorial(n-1)

n = float(raw_input("Input a number: "))
print "The fatorial is: \n", fatorial(n)