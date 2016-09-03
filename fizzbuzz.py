#!/usr/bin/env python

def fizzbuzz(n):
    str = ""
    if n%3 == 0:
        str = "fizz"

    if n%5 == 0:
        str += "buzz"

    print str if str != "" else n

    if n < 100:
        fizzbuzz(n+1)

fizzbuzz(1)