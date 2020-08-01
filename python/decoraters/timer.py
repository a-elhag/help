import time

def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        output = func(*args, **kwargs)
        end_time = time.time() - start_time
        print(end_time)
        return output
    return wrapper

@timing
def test():
    time.sleep(2)


test()

