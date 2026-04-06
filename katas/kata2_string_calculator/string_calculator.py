
def add(numbers: str) -> int:
    if numbers == "":
        return 0
    
    normalized_numbers = numbers.replace("\n", ",")
    
    return sum(map(int, normalized_numbers.split(",")))