def input_error(func):
    """Decorator for handling user input errors."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            return f"Error: {e}"
    return wrapper