def add(numbers: str) -> int:
    if numbers == "":
        return 0

    delimiter = ","
    data = numbers

    if numbers.startswith("//"):
        header, data = numbers.split("\n", 1)
        delimiter = header[2:]
        
        
        if delimiter != "," and "," in data:
            pos = data.find(",")
            raise ValueError(f"'{delimiter}' expected but ',' found at position {pos}")

    if data.endswith(delimiter) or data.endswith("\n"):
        raise ValueError("Input cannot end with a separator")
    
    parts = data.replace("\n", delimiter).split(delimiter)

    int_list = []
    for part in parts:
        if not part: 
            int_list.append(0)
        else:
            int_list.append(int(part))

    negatives = [n for n in int_list if n < 0]
    if negatives:
        neg_str = ",".join(map(str, negatives))
        raise ValueError(f"Negative number(s) not allowed: {neg_str}")

    return sum(int_list)