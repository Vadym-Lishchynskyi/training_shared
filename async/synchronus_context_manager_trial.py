class A:
    def __enter__(self):
        print("Hi, it's __enter__")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("It's __exit__ , Good Bye")


with A() as a:
    print('It is me')
