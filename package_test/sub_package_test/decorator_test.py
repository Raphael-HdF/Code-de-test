def trace(origin_func):
    def wrapper(*args, **kwargs):
        print(f"TRACE: calling {origin_func.__name__}() with arguments {args} and keyword arguments {kwargs}")
        print(f"TRACE: {origin_func.__name__}() returned '{origin_func(*args, **kwargs)}'")

    return wrapper


@trace
def format_name(first_name, last_name):
    return f"{last_name.upper()}, {first_name.capitalize()}"


format_name("David", last_name="Meyer")
