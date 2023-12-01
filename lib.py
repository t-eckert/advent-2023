def read(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def tee(val):
    print(val)
    return val
