# Q1 - Create a module with two utility functions.

# Constants
CELSIUS_VALUE = 25
KILOMETERS_VALUE = 10


def convert_celsius_to_fahrenheit(
        celsius: float
) -> float:
    """Convert Celsius to Fahrenheit."""

    return (celsius * 9 / 5) + 32


def convert_km_to_miles(
        kilometers: float
) -> float:
    """Convert kilometers to miles."""

    return kilometers * 0.621371


if __name__ == "__main__":

    print(
        f"{CELSIUS_VALUE}°C in Fahrenheit: "
        f"{convert_celsius_to_fahrenheit(CELSIUS_VALUE)}"
    )

    print(
        f"{KILOMETERS_VALUE} km in Miles: "
        f"{convert_km_to_miles(KILOMETERS_VALUE)}"
    )