from std.system import *
from std.parser import *
from std.lexer import *


'''
def run():
    data = open_file(argv[1])
    toks = lex(data)
    parse(toks)
'''

def process():
	#raw = open_f(argv[1])
	data = lex(argv[1])
	#parse(data)



if __name__ == '__main__':
	process()