"""
 замикання
"""


def function(x):
    def wrapper(y):
        def wrapper_2(z):
            print(x + y + z)

        return wrapper_2

    return wrapper


# a = function(10)(10)(10)

"""
 decorator
 
 приймає функцію на вхід
"""


def decorator(func):
    def wrapper(*args, **kwargs):
        
        func(*args, **kwargs)
        # print(10 + func(*args, **kwargs))

    return wrapper


@decorator
def add_(x, y):
    return x + y


@decorator
def sub_(x, y, **dick):
    print(**dick)
    return x - y

print(sub_(5, 4))
