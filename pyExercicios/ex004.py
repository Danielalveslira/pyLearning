anything = input('Type something: ')
print('The primitive type is {}'.format(type(anything)))
print('Is spaces? {}'.format(anything.isspace()))
print('Is all chars letters or digits? {}'.format(anything.isalnum()))
print('Is Decimal? {}'.format(anything.isdecimal()))
print('Is a Digit? {}'.format(anything.isdigit()))
print('Is LowerCase? {}'.format(anything.islower()))
print('Is UpperCase? {}'.format(anything.isupper()))
print('Is numeric? {}'.format(anything.isnumeric()))
print('Is capitalized? {}'.format(anything.istitle()))

# s.isalnum() → True if non-empty and all chars are letters or digits. ✅

# s.isalpha() → True if non-empty and all chars are letters.

# s.isascii() → True if all chars have code point < 128 (ASCII).

# s.isdecimal() → True if non-empty and all chars are decimal digits (0–9 and other Unicode decimal digits). ✅

# s.isdigit() → True if non-empty and all chars are digits (includes many Unicode digits, e.g. superscripts). ✅ 

# s.isidentifier() → True if s is a valid Python identifier (e.g. var_1), not a keyword check.

# s.islower() → True if there’s at least one cased letter and all cased letters are lowercase. ✅

# s.isnumeric() → True if non-empty and all chars are numeric (widest: includes fractions, Roman numerals, etc.).

# s.isprintable() → True if all chars are printable or whitespace like space; rejects control chars like \n, \t? (\t and \n are not printable).

# s.isspace() → True if non-empty and all chars are whitespace (spaces, tabs, newlines, etc.). ✅

# s.istitle() → True if string is titlecased (each word starts uppercase, rest lowercase), and there’s at least one cased char.

# s.isupper() → True if there’s at least one cased letter and all cased letters are uppercase. ✅