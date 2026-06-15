# Q1, Q2, Q3 - Introduction to Python

import sys


def display_welcome_message() -> None:
    print("Welcome to Python Training")


def show_python_version() -> None:
    print(f"Python version: {sys.version}")


def get_user_details() -> None:
    user_name = input("Enter your name: ")
    user_age = input("Enter your age: ")

    print(f"Hello {user_name}! You are {user_age} years old.")


if __name__ == "__main__":
    display_welcome_message()
    show_python_version()
    get_user_details()