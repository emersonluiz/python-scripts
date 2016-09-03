#!/usr/bin/env python

def anagrama(n):
    if n <= 1:
        return 1
    else:
        return n*anagrama(n-1)

str = "PYTHON"
print "The word", str, "has:", anagrama(len(str)), "anagrams."
