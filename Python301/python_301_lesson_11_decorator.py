
def my_decorator(func):
    def wrapper():
        print("Do something here.")
        func()
        print("Original function is done")
    return wrapper


@my_decorator
def my_func():
    print("My name is Andrew, I'm from Kharkiv")


my_func()
