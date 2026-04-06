
def add(numbers: str) -> int:
    if numbers == "":
        return 0
    else:
        a, b = numbers.split(",")
        return int(a) + int(b)

