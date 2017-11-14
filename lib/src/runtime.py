from std.system import *
from std.parser import *
from std.lexer import *


def process():
	data = lex(argv[1])
	parse(data)



if __name__ == '__main__':
	process()
