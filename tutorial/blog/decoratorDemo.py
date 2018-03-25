def hello(fn):
    def wrapper():
        print("begin")
        fn()
        print("end")

    return wrapper


def hi(fn):
    def wrapper(*args, **kwargs):
        for i in range(1):
            print("begin wrapper")
            fn(*args, **kwargs)
            print("end wrapper")

    return wrapper


def color(title):
    def decorator(fn):
        def wrapper():
            print(title)
            fn()

        return wrapper

    return decorator


def namer(title):
    def decorator(fn):
        def wrapper():
            print(title)
            fn()

        return wrapper

    return decorator


@namer(title="namer")
@color(title="blue")
@hi
@hello
def foo():
    print("foo")


foo()

a = 8
b = 8 if a == 7 else 9
print([i for i in range(1, 8, 1)])
print(b)
