

def fizzbuzz(number: int) -> str:
    """
    Returns "Fizz" if the number is a multiple of 3, "Buzz" if it is a multiple of 5, and "FizzBuzz" 
    if it is a multiple of both 3 and 5. If the number is not a multiple of 3 or 5, it returns the number as a string.
    """
    if number % 5 == 0 and number % 3 == 0:
        return "FizzBuzz"

    if number % 3 == 0:
        return "Fizz"
    
    if number % 5 == 0:
        return "Buzz"

    if type(number) == int:
        return str(number)
    

