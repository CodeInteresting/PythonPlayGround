# All kinds of Python Strings

str_a = "Hello Steven's \x40world"  # double quotes contain single quote
str_b = 'Big "Thanks" to \x40you'  # single quoates contain double quote

# triple double quotes span multiple lines
# can contain both single quote and double one
str_c = """How are you? 'man"
"wo\x40man'
"""

str_d = '''How are you? "man'
'm\x40an'
'''

# No matter which kind of string, it supports escape
# if you want to avoid escape, use raw string instead

str_e = r"m\x40an"

# Raw string also supports triple quotes
str_f = r"""man
\x40
"""

# f string
thing_a = "nice"
thing_b = "dog"
str_g = f"{thing_a} {thing_b}"

# Does f string support raw string?
# Wow! Surprise! It supports!
str_h = rf"{thing_a} \x40 {thing_b}"  # <output>: nice \x40 dog

print(str_a)
print(str_b)
print(str_c)
print(str_d)
print(str_e)
print(str_f)
print(str_g)
print(str_h)
