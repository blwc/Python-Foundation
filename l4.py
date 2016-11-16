def foo():
    var = 'foo variable'
    print(var)
    
def bar():
    var = 'bar variable'
    print(var)
    foo()
    print(var)
    
var = 'global variable'
print(var)
bar() # calls foo
print(var)

def foo():
    global thing
    thing = 'foo' # this is the global

def bar():
    thing = 'bar' # this is a local

def baz():
    print(thing) # this is the global

thing = 'global' # this is the global
foo()
print(thing)

def foo():
    print(thing)
    thing = 'hello from foo'

thing = 'hello from the global scope'
foo()