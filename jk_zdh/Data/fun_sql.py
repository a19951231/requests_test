
def logging(func):
    def wrapper(*args, **kwargs):
        sql=''
        return func(*args, **kwargs)
    return wrapper