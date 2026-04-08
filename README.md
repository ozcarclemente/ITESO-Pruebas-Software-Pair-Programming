# TDD Katas

Practice exercises to learn Test Driven Development following the [TDD Manifesto](https://tddmanifesto.com).

---

## Rules

Follow the three laws of TDD strictly:

1. You are not allowed to write any production code unless it is to make a failing unit test pass.
2. You are not allowed to write any more of a unit test than is sufficient to fail.
3. You are not allowed to write any more production code than is sufficient to pass the one failing unit test.

Solve only one requirement at a time. Do not read ahead.

---

## Red-Green-Refactor Cycle

- **Red** — Write a failing test for the current requirement.
- **Green** — Write the minimum production code to make it pass.
- **Refactor** — Clean up the code without breaking the test. Then repeat.

---

## Test Structure

Tests follow the **Given-When-Then** pattern using comments inside the test body:

```python
def test_should_return_number_as_string(self):
    # Given
    number = 1

    # When
    result = fizzbuzz(number)

    # Then
    self.assertEqual(result, "1")
```

---

## Stack

- Language: Python
- Testing framework: `unittest` (built-in, no installation required)

---

## Project Structure

```
katas/
├── kata1_fizzbuzz/
│   ├── fizzbuzz.py
│   └── test_fizzbuzz.py
├── kata2_string_calculator/
│   ├── string_calculator.py
│   └── test_string_calculator.py
├── kata3_password_validation/
│   ├── password_validator.py
│   └── test_password_validator.py
├── kata4_search/
│   ├── search.py
│   └── test_search.py
├── kata5_point_of_sale/
│   ├── point_of_sale.py
│   └── test_point_of_sale.py
└── kata6_banking/
    ├── account.py
    └── test_account.py
```

---

## How to Run Tests

Run all tests from the root of the project:

```bash
python -m unittest discover
```

Run tests for a specific kata:

```bash
python -m unittest katas.kata1_fizzbuzz.test_fizzbuzz
```

---

## Katas

| #   | Kata                 | Difficulty   |
| --- | -------------------- | ------------ |
| 1   | FizzBuzz             | Beginner     |
| 2   | String Calculator    | Beginner     |
| 3   | Password Validation  | Beginner     |
| 4   | Search Functionality | Beginner     |
| 5   | Point of Sale        | Intermediate |
| 6   | Banking              | Advanced     |
