class String:

def convert_to_ascii(text):
    return ''.join(str(ord(char)) for char in text)

def text_to_binary(text) :
    return ''.join(format(ord(x), 'b') for x in text)

def text_to_hex(string):
    return ''.join(format(ord(c), 'x') for c in string)

def uppercase(string):
    return string.upper()

def lowercase(string):
    return string.lower()

def length(string):
     return sum(map(lambda x:1, string))

def replace(string, old, new):
    return string.replace(old, new)

def slice(start, stop, step):
    return slice(start,stop,step)

def concat (string1, string2):
    return ' '.join([string1, string2])

def substr(string,start,stop):
    return string.substring(start,stop)
