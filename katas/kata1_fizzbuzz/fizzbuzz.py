"""Implementation of the FizzBuzz kata."""


def fizzbuzz(number: int) -> str:
    """
    Return "Fizz" if the number is divisible by 3,
    "Buzz" if it is divisible by 5,
    "FizzBuzz" if it is divisible by both,
    otherwise return the number as a string.
    """
    if number % 15 == 0:
        return "FizzBuzz"

    if number % 3 == 0:
        return "Fizz"

    if number % 5 == 0:
        return "Buzz"

    return str(number)
