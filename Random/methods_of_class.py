from types import FunctionType
import itertools

class Foo:
    def bar(self): pass
    def baz(self): pass

def methods(cls):
    return [x for x, y in cls.__dict__.items() if type(y) == FunctionType]

res = methods(Foo)  # ['bar', 'baz']
print (res)

list = [0] * 5

x = type(list)
print (x)

res = methods(x)

print (res)
