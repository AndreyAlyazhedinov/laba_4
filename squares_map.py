def main():
    numbers = range(1, 11)
    squares = list(map(lambda x: x ** 2, numbers))
    print(squares)


if __name__ == "__main__":
    main()