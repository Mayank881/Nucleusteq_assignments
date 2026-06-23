# Q1 - Import and use utility functions from a module.

from utility_functions_module import (
    convert_celsius_to_fahrenheit,
    convert_km_to_miles
)

# Constants
SAMPLE_CELSIUS = 30
SAMPLE_KILOMETERS = 15


def use_imported_functions() -> None:
    """Use utility functions imported from another module."""

    fahrenheit = convert_celsius_to_fahrenheit(
        SAMPLE_CELSIUS
    )

    miles = convert_km_to_miles(
        SAMPLE_KILOMETERS
    )

    print(
        f"{SAMPLE_CELSIUS}°C is "
        f"{fahrenheit}°F"
    )

    print(
        f"{SAMPLE_KILOMETERS} km is "
        f"{miles} miles"
    )


if __name__ == "__main__":
    use_imported_functions()