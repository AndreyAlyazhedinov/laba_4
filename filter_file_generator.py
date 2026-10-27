def read_positive_numbers(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            value = int(line)
            if value > 0:
                yield value


if __name__ == "__main__":
    print(list(read_positive_numbers("numbers.txt")))