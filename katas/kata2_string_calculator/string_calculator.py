def add(numbers: str) -> int:
    if numbers == "":
        return 0

    delimiter = ","
    if numbers.startswith("//"):
        header, numbers = numbers.split("\n", 1)
        delimiter = header[2:]

    if numbers.endswith(delimiter):
        raise ValueError("Input cannot end with a separator")

    parts = numbers.replace("\n", delimiter).split(delimiter)

    for part in parts:
        if not part.isdigit():
            raise ValueError(f"'{delimiter}' expected but '{part}' found")

    return sum(int(p) for p in parts)