def decorator1(func):
    def inner(s):
        s=s[::-1]
        func(s)
    return inner

@decorator1
def foo(string):
    print(string)



foo('Sathvk')