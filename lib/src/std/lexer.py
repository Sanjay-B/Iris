# -*- coding: utf-8 -*-
#
#  lexer.py
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

from .system import System
import time

tokens = {
	"var": {"name":[],"value":[]},
	"int": {"name":[],"value":[]},
	"bool": {"name":[],"value":[]},
	"ignored": []
}

'''
Grammer:

- Variables(var)
	- To define a variable: 
		var name = value
	- To call a variable:
		name or maybe var.name
	- Rules:
		- Can only handle string values
		- Its implied that a variable will always be a string
		- "var" must be in all lowercase, zero exception

- Integers(int)
	- To define an integer:
		int name = value
	- To call an integer:
		name or maybe int.name

- Boolean(bool)
	- To define a boolean:
		bool name = true or bool name = false
	- To call an integer:
		name or maybe bool.name

- Ignored(/)
	- To render a comment, a single "/" is placed in front of the word
	- Must have a space after the "/". 
		- Correct: / Comment
		- Wrong: /Comment
	- Comments are ignored by the lexer and parser respectively

- To replace an int, bool or var
	- name = new_value

'''

def lex(content):
	contents = open(content, "r")
	lines = contents.readlines()
	vState = 0
	iState = 0
	bState = 0
	for line in lines:
		if '/' in line:
			#print("Found Comment")
			a = line.strip().split(" ")
			c = ' '.join(a[0:])
			tokens['ignored'].append(c)
		if 'var' in line:
			a = line.strip().split(" ")
			#print(a)
			#print(a[0])
			#print(a[1])
			if not a[0] == '/' and a[1] == 'var':
				n = a[1]
				v = a[3:]
				if type(v) is not str:
					print("Systematic Error: Var-type '"+n+"' must be a string.")
					exit()

				# Limit Var duplication-based errors
				if n in tokens['var']['name']:
					print("Systematic Error: Cannot create variable object '"+n+"' more than once.")
					exit()
				else:
					#print("A")
					tokens['var']['name'].append(n)
					tokens['var']['value'].append(v)
			elif not a[0] == 'rep' and a[1] == 'var' and not a[0] == '/':
				if a[2] in tokens['var']['name']:
					print("Systematic Error: Cannot create variable object '"+n+"' more than once.")
					exit()
				else:
					#print("B")
					x = a[2]
					q = a[4]
					if type(q) is not str:
						print("Systematic Error: Var-type '"+n+"' must be a string.")
						exit()
					tokens['var']['name'].append(x)
					tokens['var']['value'].append(q)
			elif a[0] == 'var':
				#print("C")
				try:
					q = a[2]
				except IndexError:
					q = None
				if q == '=':
					#print("1")
					n = a[1]
					v = a[3]
					if type(v) is not str:
						print("Systematic Error: Var-type '"+n+"' must be a string.")
						exit()

					#print("Found Var")
					if n in tokens['var']['name']:
						print("Systematic Error: Cannot create variable object '"+n+"' more than once.")
						exit()
					else:
						#print("C")
						tokens['var']['name'].append(n)
						tokens['var']['value'].append(v)
				else:
					print("2")
					n = a[1]
					if n in tokens['var']['name']:
						print("Systematic Error: Cannot create variable object '"+n+"' more than once.")
					else:
						try:
							_w = type(a[2])
						except IndexError:
							_w = None
						#if _w is not str():
							#print("Systematic Error: Var-type '"+n+"' must be a string.")
							#exit()
						tokens['var']['name'].append(n)
						tokens['var']['value'].append(_w)
			elif a[0] == '/' and a[1] == 'var':
				#print("D")
				pass

			# Attemping to edit value of var natively
			elif a[0] in tokens['var']['name'] and a[1] == '=':
				#print("E")
				n = a[0]
				v = a[3]
				for x in tokens['var']['name']:
					if n in tokens['var']['name']:
						i = tokens['var']['name'].index(n)
						if n in tokens['var']['name']:
							tokens['var']['name'][i] = v
			else:
				#print("F")
				pass
		if 'int' in line:
			#print("Found Int")
			a = line.strip().split(" ")
			if a[0] == '/':
				b = ' '.join(a[0:])
				if b in tokens['ignored']:
					pass
				else:
					tokens['ignored'].append(b)
			elif a[0] == 'int':
				try:
					q = a[2]
				except IndexError:
					q = None
				if q == '=':
					#print("A")
					n = a[1]
					#v = a[2]
					try:
						y = int(a[3])
					except ValueError:
						print("Systematic Error: Int-type '"+n+"' must be an integer.")
						exit()
					if type(y) is not int:
						print("Systematic Error: Int-type '"+n+"' must be an integer.")
						exit()
					if n in tokens['int']['name']:
						print("Systematic Error: Cannot create integer object '"+n+"' more than once.")
						exit()
					else:
						tokens['int']['name'].append(n)
						tokens['int']['value'].append(y)
				else:
					n = a[1]
					_z = None
					if n in tokens['int']['name']:
						print("Systematic Error: Cannot create variable object '"+n+"' more than once.")
						exit()
					else:
						#print("Yes")
						#print("z = "+int(_z))
						if type(_z) == str:
							#print("Yup")
							tokens['int']['name'].append(n)
							tokens['int']['value'].append(int(_z))
						else:
							#print("No")
							#print(a)
							try:
								_z = a[3]
							except IndexError:
								_z = None
							tokens['int']['name'].append(n)
							#print("Print: "+int(z))
							tokens['int']['value'].append(_z)
			else:
				pass
		if 'bool' in line:
			#print("Found Bool")
			a = line.strip().split(" ")
			if a[0] == '/':
				b = ' '.join(a[0:])
				if b in tokens['ignored']:
					pass
				else:
					tokens['ignored'].append(b)
			elif a[0] == 'bool':
				try:
					q = a[2]
				except IndexError:
					q = None
				if q == '=':
					#print("A")
					n = a[1]
					#v = a[2]
					if n in tokens['bool']['name']:
						print("Systematic Error: Cannot create integer object '"+n+"' more than once.")
						exit()
					else:
						tokens['bool']['name'].append(n)
						tokens['bool']['value'].append(a[3])
				else:
					n = a[1]
					if n in tokens['bool']['name']:
						print("Systematic Error: Cannot create variable object '"+n+"' more than once.")
					else:
						#print("B")
						tokens['bool']['name'].append(n)
						tokens['bool']['value'].append(q)
			else:
				if v == "false":
					v = False
					tokens['bool']['name'].append(n)
					tokens['bool']['value'].append(v)
				elif v == "true":
					v = True
					tokens['bool']['name'].append(n)
					tokens['bool']['value'].append(v)
				else:
					print("Syntax Error: Attemped to create bool object '"+n+"'. Value must be boolean type.")
					exit()
		#time.sleep(2)
		v_Name = System.vList(tokens['var']['name'])
		i_Name = System.vList(tokens['int']['name'])
		b_Name = System.vList(tokens['bool']['name'])
		vName = None
		iName = None
		bName = None
		for ick in v_Name:
			vName = ick
		for kci in i_Name:
			iName = kci
		for cik in b_Name:
			bName = cik
		#print("V : "+str(vName))
		#print("I : "+str(iName))
		#print("B : "+str(bName))
		if vName is not None:
			if vName in line:
				a = line.strip().split(" ")
				#print("a - 1 = "+str(a))
				#print("a[0] = "+a[0])
				if a[0] == 'var':
					#print("Found ya")
					pass
				else:
					#print("Yes")
					#print("a - 2 = "+str(a))
					#print("Test 1:2 "+str(vName)+" == "+a[0])
					#print("Test 2:2 "+str("=")+" == "+a[1])
					if a[0] == vName and a[1] == '=':
						#print("Var toggled")
						#print("Found iName")
						#print("a - 3 = "+str(a))
						n = a[0]
						v = a[2]
						i = 0
						if n not in tokens['var']['name']:
							print("Systematic Error: Variable object '"+n+"' does not exist")
							exit()
						else:
							for x in tokens['var']['name']:
								if n in tokens['var']['name']:
									i = tokens['var']['name'].index(n)
							if n in tokens['var']['name']:
								tokens['var']['value'][i] = v
								i = 0
					elif a[0] == '/':
						b = ' '.join(a[0:])
						tokens['ignored'].append(b)
					else:
						pass
		if iName is not None:
			if iName in line:
				a = line.strip().split(" ")
				#print("a - 1 = "+str(a))
				#print("a[0] = "+a[0])
				if a[0] == 'int':
					#print("Found ya")
					pass
				else:
					#print("Yes")
					#print("a - 2 = "+str(a))
					#print("Test 1:2 "+str(vName)+" == "+a[0])
					#print("Test 2:2 "+str("=")+" == "+a[1])
					if a[0] == iName and a[1] == '=':
						#print("Var toggled")
						#print("Found iName")
						#print("a - 3 = "+str(a))
						n = a[0]
						v = a[2]
						i = 0
						if n not in tokens['int']['name']:
							print("Systematic Error: Integer object '"+n+"' does not exist")
							exit()
						else:
							for x in tokens['int']['name']:
								if n in tokens['int']['name']:
									i = tokens['int']['name'].index(n)
							if n in tokens['int']['name']:
								tokens['int']['value'][i] = v
								i = 0
					elif a[0] == '/':
						b = ' '.join(a[0:])
						tokens['ignored'].append(b)
					else:
						pass
		if bName is not None:
			if bName in line:
				a = line.strip().split(" ")
				#print("a - 1 = "+str(a))
				#print("a[0] = "+a[0])
				if a[0] == 'bool':
					#print("Found ya")
					pass
				else:
					#print("Yes")
					#print("a - 2 = "+str(a))
					#print("Test 1:2 "+str(vName)+" == "+a[0])
					#print("Test 2:2 "+str("=")+" == "+a[1])
					if a[0] == bName and a[1] == '=':
						#print("Var toggled")
						#print("Found iName")
						#print("a - 3 = "+str(a))
						n = a[0]
						v = a[2]
						i = 0
						if n not in tokens['bool']['name']:
							print("Systematic Error: Boolean object '"+n+"' does not exist")
							exit()
						else:
							for x in tokens['bool']['name']:
								if n in tokens['bool']['name']:
									i = tokens['bool']['name'].index(n)
							if n in tokens['bool']['name']:
								tokens['bool']['value'][i] = v
								i = 0
					elif a[0] == '/':
						b = ' '.join(a[0:])
						tokens['ignored'].append(b)
					else:
						pass
		
	print(tokens)
	return tokens
