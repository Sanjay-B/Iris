print("Hello World")

def convert_to_ascii(text):
    return ''.join(str(ord(char)) for char in text)

print(convert_to_ascii("lmao"))


def text_to_binary(text) :
    return ''.join(format(ord(x), 'b') for x in text)
print(text_to_binary("hello what"))


def text_to_hex(string):
    return ''.join(format(ord(c), 'x') for c in string)

print(text_to_hex("iris"))


def uppercase (string):
    return string.upper()

def lowercase (string) :
    return string.lower()

print(uppercase("iris"))
print(lowercase("IRIS"))


def length(string):
     return sum(map(lambda x:1, string))

print(length("hi world"))

def replace (string, old, new):
    return string.replace(old, new)
print(replace("I intend to live", "live", "eat"))

def slice (start, stop, step):
    return slice(start, stop, step)

def concat (string1, string2) :
    return ' '.join([string1, string2])

print(concat("Hi", "Iris is lit"))
