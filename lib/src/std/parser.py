# -*- coding: utf-8 -*-
#
#  parser.py
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

"""
The parser is quite different to what you'd expect in a normal programming language.

"""

from .system import *

std_method = ['print']

def rogue(content):
	for y in std_method:
		for yy in content['misc']:
			if y == yy:
				try:
					content['parse'][y].append(content['misc'][yy])
				except KeyError:
					try:
						content['parse'][y] = content['misc'][yy]
					except KeyError:
						print("[Iris] Bug. Report to Sanjay Bhadra(Sanjay-B)")

def parse(tokens):
	rogue(tokens)
	for m in std_method:
		for n in tokens['parse']:
			if m == n:
				System._run(m,tokens['parse'][m][0:])
