import inspect
import os
import importlib.util
import sys


class Module:

	def mcheck(arg):
		for vv in inspect.getmembers(standard.math.arg, inspect.isfunction):
			std_method[v].append(vv)

	def register(self,*arg):
		for v in arg:
			a = {v:[]}
			#print("Success")
			std_method.append(a)
			self.mcheck(v)

	def convertFileToModule(name,path):
		if name:
			if path:
				if type(name) == str:
					if type(path) == str:
						_m = importlib.util.spec_from_file_location(name,path)
						_mm = importlib.util.module_from_spec(_m)
						try: 
							_m.loader.exec_module(_mm)
						except AttributeError:
							print("Import Error: Unable to load '"+name+"'")

	def fetchStandard(module,_class):
		for v in std_lib:
			#print("Test1")
			for a in v:
				#print("Test2")
				print("--")
				print("Module: "+str(module)+", Class: "+str(_class)+" Raw: "+str(dir(inspect.isclass(module))))
				print("--")
				if _class in dir(inspect.ismethod(module)):
					print(str(module)+": Success")
				else:
					print(str(module)+": Failure")
				#print(dir(inspect.getmembers(module)))
				#if _class in dir(inspect.getmembers(module)):
					#print("Modulization works")

	def buildStandard(_module,_class,_method):
		if _class in dir(inspect.isclass(_module)):
			if _method in dir(inspect.ismethod(_class)):
				print("Found")


#C:\Users\1100276714\Desktop\Iris-legacy\lib\src\std\deps\std\standard