def logger(func):
    def wrapper(*args, **kwargs):
        arg_str = ", ".join([str(arg) for arg in args])
        kwarg_str = ", ".join([f"{key}={value}" for key, value in kwargs.items()])
        if arg_str and kwarg_str:
            print(f"{func.__name__} called with {arg_str}, {kwarg_str}")
        elif arg_str:
            print(f"{func.__name__} called with {arg_str}")
        elif kwarg_str:
            print(f"{func.__name__} called with {kwarg_str}")
        else:
            print(f"{func.__name__} called")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

add(4, 5)
square_all(1, 2, 3)
