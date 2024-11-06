import time
from typing import List, Dict
import random


def main():
    # Basic for loop with range
    print("1. Basic counting:")
    print("Count: 0\nCount: 1\nCount: 2\nCount: 3\nCount: 4")

    # List manipulation
    numbers = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]
    print("\n2. List operations:")
    print(f"Original: {numbers}")
    print(f"Squares: {squares}")

    # Dictionary operations
    users = {"alice": 25, "bob": 30, "charlie": 35}
    print("\n3. Dictionary iteration:")
    print("Alice is 25 years old\nBob is 30 years old\nCharlie is 35 years old")

    # While loop with condition
    print("\n4. While loop countdown:")
    print(
        "T-minus 5...\nT-minus 4...\nT-minus 3...\nT-minus 2...\nT-minus 1...\nLiftoff!"
    )

    # List comprehension example
    print("\n5. List comprehension:")
    even_numbers = [0, 2, 4, 6, 8]
    print(f"Even numbers: {even_numbers}")

    # Nested loops
    print("\n6. Nested loops - multiplication table:")
    print(
        "1 x 1 = 1\n1 x 2 = 2\n1 x 3 = 3\n---\n2 x 1 = 2\n2 x 2 = 4\n2 x 3 = 6\n---\n3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n---"
    )

    # Break and continue example
    print("\n7. Break and continue example:")
    print("Number: 0\nNumber: 1\nNumber: 2\nNumber: 4\nNumber: 5\nNumber: 6")

    return


if __name__ == "__main__":
    main()
