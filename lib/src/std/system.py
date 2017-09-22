#Python-Core Imports
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



'''
def doASSIGN(varname, varvalue):
    symbols[varname[7:]] = varvalue



def getVARIBLE(varname):
    varname = varname[7:]
    if varname in symbols:
        #print("TRUE")
        return symbols[varname]
    else:
        return Error_List[9]
        time.sleep(1)
        exit() #Stop current process
'''