import time
from typing import List, Dict
import random


def main():
    # Basic for loop with range
    print("1. Basic counting:")
    for i in range(5):
        print(f"Count: {i}")

    # List manipulation
    numbers = [1, 2, 3, 4, 5]
    squares = []
    print("\n2. List operations:")
    for num in numbers:
        squares.append(num**2)
    print(f"Original: {numbers}")
    print(f"Squares: {squares}")

    # Dictionary operations
    users = {"alice": 25, "bob": 30, "charlie": 35}
    print("\n3. Dictionary iteration:")
    for name, age in users.items():
        print(f"{name.capitalize()} is {age} years old")

    # While loop with condition
    print("\n4. While loop countdown:")
    countdown = 5
    while countdown > 0:
        print(f"T-minus {countdown}...")
        countdown -= 1
        time.sleep(0.5)
    print("Liftoff!")

    # List comprehension example
    print("\n5. List comprehension:")
    even_numbers = [x for x in range(10) if x % 2 == 0]
    print(f"Even numbers: {even_numbers}")

    # Nested loops
    print("\n6. Nested loops - multiplication table:")
    for i in range(1, 4):
        for j in range(1, 4):
            print(f"{i} x {j} = {i*j}")
        print("---")

    # Break and continue example
    print("\n7. Break and continue example:")
    for i in range(10):
        if i == 3:
            continue  # Skip 3
        if i == 7:
            break  # Stop at 7
        print(f"Number: {i}")

    return


if __name__ == "__main__":
    main()
