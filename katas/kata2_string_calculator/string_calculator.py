def add(numbers: str) -> int:
    if numbers == "":
        return 0

    normalized_numbers = numbers.replace("\n", ",")

    if normalized_numbers.endswith(","):
        raise ValueError("Input cannot end with a comma")

    number_list = normalized_numbers.split(",")

    return sum(int(n) if n else 0 for n in number_list)
