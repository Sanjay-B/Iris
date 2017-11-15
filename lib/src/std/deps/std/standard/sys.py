# -*- coding: utf-8 -*-
#
#  sys.py
#  Iris -> Standard
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

__author__ = "Sanjay-B(Sanjay Bhadra)"

'''
The Standard Library is core methods and diction that Iris comes with natively
that doesn't require the load of modules. All methods contained within this
file are considered global classes/methods. 
'''

class Native:

	def _print(obj):
		if obj:
			for ss in obj:
				if type(ss) == str:
					sss = ss.replace('"', '')
					print(sss)
				elif type(ss) == list:
					for dd in ss:
						for ddd in dd:
							dddd = ddd.replace('"', '')
							print(dddd)
				elif type(ss) == int:
					print(str(ss))
				else:
					print(str(ss))
		else:
			print("Error: No required 1st parameter for print <object>")
			exit()
