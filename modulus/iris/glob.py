import builtins
import os

class __Globals__:
	
	def load():

		# Temporary 
		builtins.std_method = []

		# Bloated Stack
		builtins.tokens = {
			"var": {"name": [],"value": []},
			"int": {"name": [],"value": []},
			"bool": {"name": [],"value": []},
			"ignored": [],
			"parse": {},
			"misc": {},
			"main_thread": [], # Main Thread; priority execution
			"imports": {"standard": {"math": False}, "other": []}
		}

		# Reserved Words
		builtins.def_keywords = [
			'/',
			'//',
			'var',
			'int',
			'bool',
			'if',
			'else',
			'define',
			'end',
			'__'
		]

		# Standard Library - Sub libs
		# All known availiable classes
		builtins.std_lib = {
			"math",
			"string"
		}

		# Paths
		builtins.path = {
			"desktop": str(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')),
			"iris_main_path": None,
			"current_path": None
		}

		# Versions
		builtins.version = {
			"Iris": "Iris-legacy"
		}
		