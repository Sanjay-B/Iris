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

from .system import System, Systematic
import time

tokens = {
	"var": {"name": [],"value": []},
	"int": {"name": [],"value": []},
	"bool": {"name": [],"value": []},
	"ignored": [],
	"parse": {},
	"misc": {},
	"main_thread": []
}

def lex(content):
	contents = open(content, "r")
	lines = contents.readlines()
	global if_state
	global else_state
	global method_state
	global event_state
	global method_name
	passed = False
	if_state = False
	else_state = False
	method_state = False
	event_state = False
	weird_case = False
	detected_space_below = False
	method_called = False
	under_method_called = False
	num_call_methods = 0
	num_call_events = 0
	line_number = 0

	# Reserved words
	def_keywords = ['/','//','var','int','bool','if','else','define']

	# Should figure this out soon tbh
	global std_method
	std_method = ['print']

	parameters = None
	def_placeholder = []
	for line in lines:
		line_number = line_number + 1
		#print("Line Number : "+str(line_number))
		if '/' in line:
			a = line.strip().split(" ")
			c = ' '.join(a[0:])
			tokens['ignored'].append(c)
		if 'var' in line:
			a = line.strip().split(" ")
			if not a[0] == '/' and a[1] == 'var':
				n = a[1]
				v = a[3:]
				if type(v) is not str:
					print("Systematic Error: Var-type '"+n+"' must be a string. Line: "+str(line_number))
					exit()

				# Limit Var duplication-based errors
				if n in tokens['var']['name']:
					print("Systematic Error: Cannot create variable object '"+n+"' more than once. Line: "+str(line_number))
					exit()
				else:
					tokens['var']['name'].append(n)
					tokens['var']['value'].append(v)
			elif not a[0] == 'rep' and a[1] == 'var' and not a[0] == '/':
				if a[2] in tokens['var']['name']:
					print("Systematic Error: Cannot create variable object '"+n+"' more than once. Line: "+str(line_number))
					exit()
				else:
					x = a[2]
					q = a[4]
					if type(q) is not str:
						print("Systematic Error: Var-type '"+n+"' must be a string. Line: "+str(line_number))
						exit()
					tokens['var']['name'].append(x)
					tokens['var']['value'].append(q)
			elif a[0] == 'var':
				try:
					q = a[2]
				except IndexError:
					q = None
				if q == '=':
					n = a[1]
					v = a[3]
					if type(v) is not str:
						print("Systematic Error: Var-type '"+n+"' must be a string. Line: "+str(line_number))
						exit()

					if n in tokens['var']['name']:
						print("Systematic Error: Cannot create variable object '"+n+"' more than once. Line: "+str(line_number))
						exit()
					else:
						tokens['var']['name'].append(n)
						tokens['var']['value'].append(v)
				else:
					n = a[1]
					if n in tokens['var']['name']:
						print("Systematic Error: Cannot create variable object '"+n+"' more than once. Line: "+str(line_number))
					else:
						try:
							_w = type(a[2])
						except IndexError:
							_w = None
						tokens['var']['name'].append(n)
						tokens['var']['value'].append(_w)
			elif a[0] == '/' and a[1] == 'var':
				pass

			# Attemping to edit value of var natively
			elif a[0] in tokens['var']['name'] and a[1] == '=':
				n = a[0]
				v = a[3]
				for x in tokens['var']['name']:
					if n in tokens['var']['name']:
						i = tokens['var']['name'].index(n)
						if n in tokens['var']['name']:
							tokens['var']['name'][i] = v
			else:
				pass
		if 'int' in line:
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
					n = a[1]
					try:
						y = int(a[3])
					except ValueError:
						print("Systematic Error: Int-type '"+n+"' must be an integer. Line: "+str(line_number))
						exit()
					if type(y) is not int:
						print("Systematic Error: Int-type '"+n+"' must be an integer. Line: "+str(line_number))
						exit()
					if n in tokens['int']['name']:
						print("Systematic Error: Cannot create integer object '"+n+"' more than once. Line: "+str(line_number))
						exit()
					else:
						tokens['int']['name'].append(n)
						tokens['int']['value'].append(y)
				else:
					n = a[1]
					_z = None
					if n in tokens['int']['name']:
						print("Systematic Error: Cannot create variable object '"+n+"' more than once. Line: "+str(line_number))
						exit()
					else:
						if type(_z) == str:
							tokens['int']['name'].append(n)
							tokens['int']['value'].append(int(_z))
						else:
							try:
								_z = a[3]
							except IndexError:
								_z = None
							tokens['int']['name'].append(n)
							tokens['int']['value'].append(_z)
			else:
				pass
		if 'bool' in line:
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
					n = a[1]
					if n in tokens['bool']['name']:
						print("Systematic Error: Cannot create boolean object '"+n+"' more than once. Line: "+str(line_number))
						exit()
					else:
						tokens['bool']['name'].append(n)
						tokens['bool']['value'].append(a[3])
				else:
					n = a[1]
					if n in tokens['bool']['name']:
						print("Systematic Error: Cannot create boolean object '"+n+"' more than once. Line: "+str(line_number))
					else:
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
					print("Syntax Error: Attemped to create boolean object '"+n+"'. Value must be boolean type. Line: "+str(line_number))
					exit()

		v_Name = Systematic.vList(tokens['var']['name'])
		i_Name = Systematic.iList(tokens['int']['name'])
		b_Name = Systematic.bList(tokens['bool']['name'])
		vName = None
		iName = None
		bName = None
		for ick in v_Name:
			vName = ick
		for kci in i_Name:
			iName = kci
		for cik in b_Name:
			bName = cik
		if vName is not None:
			if vName in line:
				a = line.strip().split(" ")
				if a[0] == 'var':
					pass
				else:
					if a[0] == vName and a[1] == '=':
						n = a[0]
						v = a[2]
						i = 0
						if n not in tokens['var']['name']:
							print("Systematic Error: Variable object '"+n+"' does not exist Line: "+str(line_number))
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
				if a[0] == 'int':
					pass
				else:
					if a[0] == iName and a[1] == '=':
						n = a[0]
						v = a[2]
						i = 0
						if n not in tokens['int']['name']:
							print("Systematic Error: Integer object '"+n+"' does not exist Line: "+str(line_number))
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
				if a[0] == 'bool':
					pass
				else:
					if a[0] == bName and a[1] == '=':
						n = a[0]
						v = a[2]
						i = 0
						if n not in tokens['bool']['name']:
							print("Systematic Error: Boolean object '"+n+"' does not exist Line: "+str(line_number))
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
		if 'if' in line:
			a = line.strip().split(" ")
			if_state = True
			if method_state == False:
				if a[2] == "==":
					if a[4] == "do":
						x = a[1]
						y = a[3]
						is_var = False
						is_int = False
						is_bool = False
						if x in tokens['var']['name']:
							is_var = True
						elif x in tokens['int']['name']:
							is_int = True
						elif x in tokens['bool']['name']:
							is_bool = True

						#print(is_var,is_int,is_bool)
						obj_value = None
						if is_var == True:
							is_var = None
							is_int = None
							is_bool = None
							if x in tokens['var']['name']:
								i = tokens['var']['name'].index(x)
								obj_value = tokens['var']['value'][i]

							if obj_value == y:
								passed = True
							else:
								passed = False
						elif is_int == True:
							is_var = None
							is_int = None
							is_bool = None
							if x in tokens['int']['name']:
								i = tokens['int']['name'].index(x)
								obj_value = tokens['int']['value'][i]

							if obj_value == y:
								passed = True
							else:
								passed = False
						elif is_bool == True:
							is_var = None
							is_int = None
							is_bool = None
							if x in tokens['bool']['name']:
								i = tokens['bool']['name'].index(x)
								obj_value = tokens['bool']['value'][i]

							if obj_value == y:
								passed = True
							else:
								passed = False
					else:
						print("Systematic Error: Missing 'do' at if statement Line: "+str(line_number))
						exit()
				else:
					print("Logical Error: Unknown operator-type '"+a[2]+"' Line: "+str(line_number))
					exit()
			elif method_state == True:
				#print(a)
				if a[2] == "==":
					if a[4] == "do":
						x = a[1]
						y = a[3]
						is_var = False
						is_int = False
						is_bool = False
						if x in tokens['var']['name']:
							is_var = True
						elif x in tokens['int']['name']:
							is_int = True
						elif x in tokens['bool']['name']:
							is_bool = True

						#print(is_var,is_int,is_bool)
						obj_value = None
						if is_var == True:
							is_var = None
							is_int = None
							is_bool = None
							if x in tokens['var']['name']:
								i = tokens['var']['name'].index(x)
								obj_value = tokens['var']['value'][i]

							if obj_value == y:
								passed = True
							else:
								passed = False
						elif is_int == True:
							is_var = None
							is_int = None
							is_bool = None
							if x in tokens['int']['name']:
								i = tokens['int']['name'].index(x)
								obj_value = tokens['int']['value'][i]

							if obj_value == y:
								passed = True
							else:
								passed = False
						elif is_bool == True:
							is_var = None
							is_int = None
							is_bool = None
							if x in tokens['bool']['name']:
								i = tokens['bool']['name'].index(x)
								obj_value = tokens['bool']['value'][i]

							if obj_value == y:
								passed = True
							else:
								passed = False
					else:
						print("Systematic Error: Missing 'do' at if statement Line: "+str(line_number))
						exit()
				else:
					print("Logical Error: Unknown operator-type '"+a[2]+"' Line: "+str(line_number))
					exit()
		if 'else' in line:
			if if_state == True and passed == False:
				else_state = True
				if_state = False
				passed = False
			elif if_state == True and passed == True:
				else_state = False
				if_state = True
				passed = True
			else:
				pass

		# No idea how nested if-else statements are going to work..
		if else_state == False and passed == True and if_state == True and not 'else' in line and not 'if' in line and method_state == False:
			a = line.strip().split(" ")
			if type(a) == list:
				for b in a:
					if b == '' or b == "":
						pass
			else:
				tokens['parse'] = {a[0]:[a[1]]}
				if_state = False
				else_state = False
				passed = False

		if else_state == True and passed == False and if_state == False and not 'else' in line and not 'if' in line and method_state == False:
			a = line.strip().split(" ")
			if type(a) == list:
				for b in a:
					if b == '' or b == "":
						pass
			else:
				tokens['parse'] = {a[0]:[a[1]]}
				if_state = False
				else_state = False
				passed = False

		if 'define' in line:
			a = line.strip().split(" ")
			#print(a)
			method_name = None
			method_verified = False
			event_verified = False
			method_case = False
			method_table_found = False
			disallowed_keywords = ["if","else","do","==","var","int","bool"]
			if a[0:] in disallowed_keywords:
				print("Systematic Error: Method construction cannot contain conditionals, <Object-type> assignment or rogue values Line: "+str(line_number))
				exit()
			if a[0:] in def_placeholder:
				print("Found method-type")
				pass
			if '//' in a[0:]:
				pass
			if a[1]:
				method_name = a[1]
			else:
				print("Systematic Error: Method constructed incorrectly; name not found Line: "+str(line_number))
				exit()
			if a[0] == "define":
				if a[2] == "->":
					totalCount = 0
					for v in a:
						totalCount = totalCount + 1
					i = (totalCount - 3)
					if a[3] == "[" and a[totalCount - 3] == "]": 
						parameters = (a[4:i])
						if a[totalCount - 2] == ":":
							if a[totalCount - 1] == "()":
								#print("Method")
								method_case = True
								num_call_methods = (num_call_methods + 1)
								for xx in tokens['parse']:
									if xx == "methods":
										method_table_found = True
								if method_case == True and method_table_found == True:
									tokens['parse']['methods'].append({method_name:{"num":num_call_methods, "params":[parameters], "action":[], "call":[]}})
									def_placeholder.append(method_name)
									method_state = True
									method_case = False
									method_table_found = False
									under_method_called = True
									#method_name = None
									#print(tokens)
								elif method_case == True and method_table_found == False:
									tokens['parse'] = {"methods":{method_name:{"num":num_call_methods, "params":[parameters], "action":[], "call":[]}}}
									def_placeholder.append(method_name)
									method_state = True
									method_case = False
									method_table_found = False
									under_method_called = True
									#method_name = None
									#print(tokens)
								else:
									print("Method Bug")
									exit()
							elif a[totalCount - 1] == "@":
								print("Event")
								pass # I'll parse events later as they requre more in-depth work
					else:
						print("Systematic Error: Missing bracket at '"+method_name+"'; infinite parameter clause disallowed Line: "+str(line_number))
						exit()
				else:
					print("Systematic Error: Missing '->' at method-class '"+method_name+"' Line: "+str(line_number))
					exit()

		if 'end' in line:
			a = line.strip().split(" ")
			if a[0] == "end":
				if len(a) == 1:
					if method_state == True:
						method_state = False
					else:
						print("Systematic Error: 'end' missing parent 'define' structure Line: "+str(line_number))
				else:
					print("Wrong 2")
			else:
				print("Wrong 1")
		# Sneaky little spaces
		if " " in line:
			if detected_space_below == True:
				detected_space_below = False
			elif detected_space_below == False:
				detected_space_below = True
			else:
				print("Space Bug")

		# Check for user-made method calls
		for m in def_placeholder:
			if m in line:
				#print("Found Method call in '"+str(line)+"'")
				a = line.strip().split(" ")
				if a[0] in def_keywords:
					pass
				elif a[0] in def_placeholder:
					if a[1] == "=>":
						#print("Method Valid")
						method_called = True
						tokens['main_thread'].append({line_number:{a[0]:[parameters]}})
					else:
						print("Systematic Error: Invalid method construction Line: "+str(line_number))
						exit()
				else:
					print("Systematic Error: method '"+a[0]+"' was never contructed Line: "+str(line_number))
					exit()

		# Check for standard lib calls
		for n in std_method:
			if n in line:
				a = line.strip().split(" ")
				if a[0] in def_keywords:
					pass
				elif a[0] in std_method:
					if a[1] == "=>":
						method_called = True
						tokens['main_thread'].append({line_number:{a[0]:[a[2:]]}})
					else:
						print("Systematic Error: Invalid method construction Line: "+str(line_number))
						exit()
				else:
					print("Systematic Error: method '"+a[0]+"' was never contructed Line: "+str(line_number))
					exit()

		# Need to check for imports then, their method calls.. : (


		if method_state == True and passed == True and detected_space_below == False:
			#print("Rarity toggled")
			#print("Line : "+str(a))
			try:
				if {a[0]:[a[2:]]} in tokens['parse']['methods'][method_name]['action']:
					#print("Duplicated string")
					pass
				else:
					#print("toggled sad")
					tokens['parse']['methods'][method_name]['action'].append({a[0]:[a[2:]]})
			except KeyError:
				print("Method bug 2")

		# Find any rogue things and such
		else:
			
			# Ignore comments
			if a[0] == "/" or a[0] == "//":
				pass
			elif if_state == True and method_state == True and weird_case == False:
				weird_case = True
				#print("passed")
				pass
			elif if_state == True and method_state == True and weird_case == True and detected_space_below == False:
				#print("Rarity 2 toggled")
				try:
					print("Okay")
					if method_called == True and under_method_called == True and detected_space_below == True:
						tokens['parse']['methods'][method_name]['action'].append({a[0]:[a[2:]]})
					else:
						pass
				except KeyError:
					print("Method bug 2")
			elif method_state == True and detected_space_below == False and under_method_called == True and if_state == True and weird_case == True:
				if a[0] == "define" or a[0] == "else" or a[0] == "if":
					print("saweuhd")
					pass
				else:  
					try:
						print("whagsa")
						tokens['parse']['methods'][method_name]['action'].append({a[0]:[a[2:]]})
					except KeyError:
						print("Method Bug 3")
			else:
				try:
					if a[0] in def_keywords:
						pass
					elif type(a[1:]) == str:
						tokens['misc'] = {a[0]:str(a[1:])}
					else:
						tokens['misc'] = {a[0]:[a[1:]]}
				except IndexError:
					pass # Rare exception

	#print("Method State = "+str(method_state))
	#print("If State = "+str(if_state))
	#print(str(def_placeholder))
	#print(str(line_number))
	#print("--")
	#print("If state : "+str(if_state))
	#print("Method state : "+str(method_state))
	#print("Weird case : "+str(weird_case))
	#print("Detected_space_below : "+str(detected_space_below))
	#print("Method called : "+str(method_called))
	#print("--")
	print(tokens)
	return tokens


#python C:\Users\1100276714\Desktop\Iris-legacy\lib\src\runtime.py C:\Users\1100276714\Desktop\Iris-legacy\tests\test6.ris
#python C:\Users\sanja\Desktop\Iris-legacy\lib\src\runtime.py C:\Users\sanja\Desktop\Iris-legacy\tests\test6.ris
