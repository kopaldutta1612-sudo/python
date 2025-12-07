#!/usr/bin/env python3
"""
Simple Python sample: CLI demo that computes Fibonacci,
sorts numbers, and shows both interactive and non-interactive modes.
"""
import argparse
import sys


def fib(n: int) -> int:
    if n <= 0:
        return 0
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def sort_numbers(nums):
    return sorted(nums)


def demo():
    print("Demo run — computing some example values:")
    n = 10
    print(f"Fibonacci({n}) = {fib(n)}")
    arr = [5, 1, 4, 3, 2]
    print(f"Original list: {arr}")
    print(f"Sorted list:   {sort_numbers(arr)}")


def interactive():
    print("Interactive mode. Enter commands or 'q' to quit.")
    while True:
        try:
            cmd = input("Choose (fib/sort/q): ").strip().lower()
        except EOFError:
            print()
            break
        if cmd in ("q", "quit", "exit"):
            break
        if cmd == "fib":
            s = input("Enter n (integer): ")
            try:
                n = int(s)
                print(f"Fibonacci({n}) = {fib(n)}")
            except ValueError:
                print("Please enter a valid integer.")
        elif cmd == "sort":
            s = input("Enter numbers separated by spaces: ")
            try:
                nums = list(map(float, s.split()))
                print(sort_numbers(nums))
            except ValueError:
                print("Enter valid numbers separated by spaces.")
        else:
            print("Unknown command. Use 'fib', 'sort', or 'q'.")


def parse_args():
    p = argparse.ArgumentParser(description="Sample Python demo")
    p.add_argument("--demo", action="store_true", help="run non-interactive demo")
    return p.parse_args()


if __name__ == "__main__":
    args = parse_args()
    if args.demo:
        demo()
        sys.exit(0)
    interactive()
