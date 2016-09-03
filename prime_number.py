#!/usr/bin/env python

for i in range(1,101):
    cont = 2

    for j in range(1, i+1):
       if (i % j) == 0:
           cont -= 1

    if cont == 0:
       print i, "IS PRIME!!!"
    else:
       print i, "is not prime!"
