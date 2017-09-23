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

- Replace(rep)
	- To define an replacement:
		rep OPTION name = new_value
	- Rules:
		- Options: var, bool
		- Object must exist prior to changing it's value

- Ignored(/)
	- To render a comment, a single "/" is placed in front of the word
	- Comments are ignored by the lexer and parser respectively



'''

def lex(content):
	contents = open(content, "r")
	lines = contents.readlines()
	for line in lines:
		if '/' in line:
			#print("Found Comment")
			a = line.strip().split(" ")
			c = ' '.join(a[0:])
			tokens['ignored'].append(c)
		if 'var' in line:
			#print("Found Var")
			a = line.strip().split(" ")
			if a[0] == 'rep':
				pass
			if a[1] == 'rep':
				pass
			n = a[1]
			v = a[3:]

			# Limit Var duplication-based errors
			if n in tokens['var']['name']:
				print("Sytematic Error: Cannot create variable object '"+n+"' more than once.")
				exit()
			else:
				tokens['var']['name'].append(n)
				tokens['var']['value'].append(v)
		if 'int' in line:
			#print("Found Int")
			a = line.strip().split(" ")
			if a[0] == '/':
				b = ' '.join(a[0:])
				if b in tokens['ignored']:
					pass
				else:
					tokens['ignored'].append(b)
			else:
				i = a[1]
				v = a[3:]
				if i in tokens['int']['name']:
					print("Systematic Error: Cannot create integer object '"+i+"' more than once.")
					exit()
				else:
					tokens['int']['name'].append(i)
					tokens['int']['value'].append(v)
		'''
		# Keyword: rep needs to be fixed
		if 'rep' in line:
			#print("Found Rep")
			a = line.strip().split(" ")
			is_value = 0
			if a[0] == '/':
				b = ' '.join(a[0:])
				if b in tokens['ignored']:
					pass
				else:
					tokens['ignored'].append(b)
			else:
				n = a[2]
				v = a[4:]
				i = 0
				q = 0
				print(a[1])
				if a[1] == 'var' and is_value == 0:
					if n not in tokens['var']['name']:
						print("Var '"+n+"' does not exist")
					else:
						print("Found Var")
						is_value = 1
						for x in tokens['var']['name']:
							if n in tokens['var']['name']:
								i = tokens['var']['name'].index(n)
						if n in tokens['var']['name']:
							tokens['var']['name'][i] = v
							i = 0
							is_value = 0
		'''
				if a[1] == 'bool' and is_value == 0:
					if n not in tokens['bool']['name']:
						print("Bool '"+n+"' does not exist")
					else:
						print("Found Bool")
						is_value = 1
						for x in tokens['bool']['name']:
							if n in tokens['bool']['name']:
								q = tokens['bool']['name'].index(n)
						if n in tokens['bool']['name']:
							tokens['bool']['name'][q] = v
							q = 0
							is_value = 0
				if a[1] is not 'var' and is_value == 0 or a[1] is not 'bool' and is_value == 0:
					print("Systematic Error: Cannot replace none-type value.")
					exit()		
		if 'bool' in line:
			#print("Found Bool")
			a = line.strip().split(" ")
			n = a[1]
			v = a[3]
			if n in tokens['bool']['name']:
				print("Systematic Error: Cannot create bool object '"+n+"' more than once.")
				exit()
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

	print(tokens)
	return tokens
