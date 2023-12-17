
import time

def retry(max_retries=3):
    """
        Decorator for retrying a function a given number of time.
        defualt number of retry is 3 times
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries:
                        raise e
                    time.sleep(1)
            return None
        return wrapper
    return decorator