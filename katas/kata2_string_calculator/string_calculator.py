def add(numbers: str) -> int:
    if numbers == "":
        return 0

    delimiter = ","
    data = numbers
    errors = []

    if numbers.startswith("//"):
        header, data = numbers.split("\n", 1)
        delimiter = header[2:]

    if data.endswith(delimiter) or data.endswith("\n"):
        raise ValueError("Input cannot end with a separator")

    parts = data.replace("\n", delimiter).replace(",", delimiter).split(delimiter)

    int_list = []
    for part in parts:
        if not part:
            int_list.append(0)
        else:
            try:
                int_list.append(int(part))
            except ValueError:
                pass

    negatives = [n for n in int_list if n < 0]
    if negatives:
        neg_str = ",".join(map(str, negatives))
        errors.append(f"Negative number(s) not allowed: {neg_str}")

    if delimiter != ",":
        i = 0
        while i < len(data):
            if data[i : i + len(delimiter)] == delimiter:
                i += len(delimiter)
            elif data[i] == "\n" or data[i].isdigit() or data[i] == "-":
                i += 1
            else:
                errors.append(
                    f"'{delimiter}' expected but '{data[i]}' found at position {i}."
                )
                i += 1
        
    if errors:
        raise ValueError("\n".join(errors))

    return sum(int_list)
