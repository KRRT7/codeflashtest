import time
from typing import List, Dict
import random


def main():
    output = []

    # Basic for loop with range
    output.append("1. Basic counting:")
    output.append("\n".join(f"Count: {i}" for i in range(5)))

    # List manipulation
    numbers = [1, 2, 3, 4, 5]
    output.append("\n2. List operations:")
    output.append(f"Original: {numbers}")
    output.append(f"Squares: {[num**2 for num in numbers]}")

    # Dictionary operations
    users = {"alice": 25, "bob": 30, "charlie": 35}
    output.append("\n3. Dictionary iteration:")
    output.append(
        "\n".join(
            f"{name.capitalize()} is {age} years old" for name, age in users.items()
        )
    )

    # While loop with condition
    output.append("\n4. While loop countdown:")
    countdown = 5
    while countdown > 0:
        output.append(f"T-minus {countdown}...")
        countdown -= 1
    output.append("Liftoff!")

    # List comprehension example
    output.append("\n5. List comprehension:")
    output.append(f"Even numbers: {[x for x in range(10) if x % 2 == 0]}")

    # Nested loops
    output.append("\n6. Nested loops - multiplication table:")
    output.append(
        "\n".join(
            "---\n".join(f"{i} x {j} = {i * j}" for j in range(1, 4))
            for i in range(1, 4)
        )
        + "\n---"
    )

    # Break and continue example
    output.append("\n7. Break and continue example:")
    output.append("\n".join(f"Number: {i}" for i in range(10) if i != 3 and i < 7))

    print("\n".join(output))

    return


if __name__ == "__main__":
    main()
