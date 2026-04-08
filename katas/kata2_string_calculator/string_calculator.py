"""Implementation of the String Calculator kata."""


def _extract_delimiter_and_data(numbers: str) -> tuple[str, str]:
    """Extract the delimiter and the numeric data from the input."""
    if numbers.startswith("//"):
        header, data = numbers.split("\n", 1)
        return header[2:], data

    return ",", numbers


def _build_int_list(parts: list[str]) -> list[int]:
    """Convert parts into integers, treating empty parts as zero."""
    int_list = []

    for part in parts:
        if part == "":
            int_list.append(0)
            continue

        try:
            int_list.append(int(part))
        except ValueError:
            continue

    return int_list


def _find_invalid_separator_errors(data: str, delimiter: str) -> list[str]:
    """Return errors for invalid characters when using a custom delimiter."""
    if delimiter == ",":
        return []

    errors = []
    i = 0

    while i < len(data):
        if data[i : i + len(delimiter)] == delimiter:
            i += len(delimiter)
        elif data[i].isdigit() or data[i] in {"\n", "-"}:
            i += 1
        else:
            errors.append(
                f"'{delimiter}' expected but '{data[i]}' found at position {i}."
            )
            i += 1

    return errors


def add(numbers: str) -> int:
    """Return the sum of numbers in a string following defined rules."""
    if numbers == "":
        return 0

    delimiter, data = _extract_delimiter_and_data(numbers)

    if data.endswith(delimiter) or data.endswith("\n"):
        raise ValueError("Input cannot end with a separator")

    parts = data.replace("\n", delimiter).replace(",", delimiter).split(delimiter)
    int_list = _build_int_list(parts)

    errors = []

    negatives = [number for number in int_list if number < 0]
    if negatives:
        neg_str = ",".join(str(number) for number in negatives)
        errors.append(f"Negative number(s) not allowed: {neg_str}")

    errors.extend(_find_invalid_separator_errors(data, delimiter))

    if errors:
        raise ValueError("\n".join(errors))

    return sum(number for number in int_list if number <= 1000)
