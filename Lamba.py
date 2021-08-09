
f = lambda x, y, z: x + y + z

f2 = lambda first="Steven", last="Shao": first + " " + last

print(f(1, 2, 3))

print(f2())

def funcFactory(x):
    def inner():
        nonlocal x
        y = x
        x += 1
        return y
    return inner

counter = funcFactory(5)
print(counter())
print(counter())
print(counter())
print(counter())