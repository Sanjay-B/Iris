from .system import *
'''
Process:

- - 1). Initialize Variables [ ]
 |
  - 2). Initialize Integers [ ]
'''

# python C:\Users\1100276714\Desktop\coding\lang\lib\src\runtime.py C:\Users\1100276714\Desktop\coding\lang\tests\test1.ris

def parse(tokens):
	i = 0
	while(i < len(tokens)):

		if tokens['ignored']:
			#print("Found Ignored")
			i += 1
			pass

		if tokens['var']['name']:
			#pring("Found Var")
			i += 2

		if tokens['int']['name']:
			#print("Found Int")
			i += 3


