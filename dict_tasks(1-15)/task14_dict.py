#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------
#
#   Write a Python program to sort a given dictionary by key.
#
#---------------------------------------------------------------------------------------------

md = {'b': 2, 'c': 4, 'f': 12, 'a': 122}

md = dict(sorted(md.items()))

print(md)

