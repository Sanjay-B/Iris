# -*- coding: utf-8 -*-
#
#  system.py
#  Iris
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2017 Sage Technologies LLC. All rights reserved.
#

"""
The MIT License (MIT)

Copyright © 2017 Sage Technologies LLC. All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, modify, merge, publish and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from sys import *
import time 

o_stack = []
n_stack = []
sym = {}

class System:
    def openf(filename):
        data = open(filename, "r").read()
        data += "<EOF>"
        return data

    def vList(_list):
        for v in _list:
            a = v
            yield a
            del a

    def iList(_list):
        for i in _list:
            return i

    def bList(_list):
        for b in _list:
            return b

class Systematic:
    def vAssign(name,value):
        sym[name] = value

    def gVar(name):
        if name in sym:
            return sym[name]
        else:
            return print("[Error] Variable referenced before assignment")

    def gEval(value):
        return eval(value)

    def aQuote(name):
        return "'"+name+"'"

    def _loop(_array):
        for item in _array:
            return item

    def _print(_obj):
        a = str(_obj)
        print(a)
