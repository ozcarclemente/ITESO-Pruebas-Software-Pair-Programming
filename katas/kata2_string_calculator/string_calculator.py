
def add(numbers: str) -> int:
    if numbers == "":
        return 0
    else:
        return sum(map(int, numbers.split(",")))


