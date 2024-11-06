import time
from typing import List, Dict
import random


def main():
    # Basic for loop with range
    print("1. Basic counting:")
    print("\n".join(f"Count: {i}" for i in range(5)))

    # List manipulation
    numbers = [1, 2, 3, 4, 5]
    squares = [num**2 for num in numbers]
    print("\n2. List operations:")
    print(f"Original: {numbers}")
    print(f"Squares: {squares}")

    # Dictionary operations
    users = {"alice": 25, "bob": 30, "charlie": 35}
    print("\n3. Dictionary iteration:")
    print(
        "\n".join(
            f"{name.capitalize()} is {age} years old" for name, age in users.items()
        )
    )

    # While loop with condition
    print("\n4. While loop countdown:")
    countdown = 5
    while countdown > 0:
        print(f"T-minus {countdown}...")
        countdown -= 1
    print("Liftoff!")

    # List comprehension example
    print("\n5. List comprehension:")
    even_numbers = [x for x in range(10) if x % 2 == 0]
    print(f"Even numbers: {even_numbers}")

    # Nested loops
    print("\n6. Nested loops - multiplication table:")
    print(
        "\n".join(
            "---\n".join(f"{i} x {j} = {i*j}" for j in range(1, 4)) for i in range(1, 4)
        )
    )
    print("---")

    # Break and continue example
    print("\n7. Break and continue example:")
    print("\n".join(f"Number: {i}" for i in range(10) if i != 3 and i < 7))

    return


if __name__ == "__main__":
    main()
