def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, type_):
                    print(f"Argument {arg} is not of type {type_}")
                    return False
                if len(str(arg)) > max_length:
                    print(f"Argument {arg} exceeds maximum length of {max_length}")
                    return False
                for symbol in contains:
                    if symbol not in str(arg):
                        print(f"Argument {arg} does not contain {symbol}")
                        return False
            return func(*args, **kwargs)
        return wrapper
    return decorator

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
