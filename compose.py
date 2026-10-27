from functools import reduce


def compose(*functions):
    return reduce(lambda f, g: lambda x: g(f(x)), functions)


if __name__ == "__main__":
    add_one = lambda x: x + 1
    square = lambda x: x ** 2
    to_string = lambda x: f"Результат: {x}"

    pipeline = compose(add_one, square, to_string)
    print(pipeline(3))