import functools

def logger(message: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f"✅ Book '{args[1].title}' {message}")
            return result
        return wrapper
    return decorator
