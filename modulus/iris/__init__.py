# By Sanjay-B(Sanjay Bhadra)

from .glob import __Globals__
__Globals__.load()
from .modules import Module
import builtins
import sys
#sys.path.append(path['desktop']+'/'+version['Iris']+'/lib/src/std/deps/std/standard')
#math = Module.convertFileToModule('math', path['desktop']+'/'+version['Iris']+'/lib/src/std/deps/std/standard/math/math.py')
#string = Module.convertFileToModule('strings', path['desktop']+'/'+version['Iris']+'/lib/src/std/deps/std/standard/strings/string.py')
#print("Module Math: "+str(math))
#print("Module String: "+str(string))
#import maths
#import strings
#Module.fetchStandard(maths,"Maths")
#Module.fetchStandard(strings,"String")