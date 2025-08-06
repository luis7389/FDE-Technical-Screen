def sort(width, height, length, mass):
    """
    Sorts a package into the correct stack based on its dimensions and mass.

    Args:
        width (float): Width of the package in centimeters.
        height (float): Height of the package in centimeters.
        length (float): Length of the package in centimeters.
        mass (float): Mass of the package in kilograms.

    Returns:
        str: The name of the stack ("STANDARD", "SPECIAL", or "REJECTED").
    """
    volume = width * height * length
    bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    heavy = mass >= 20

    # Use ternary operator as required
    return (
        "REJECTED" if bulky and heavy
        else "SPECIAL" if bulky or heavy
        else "STANDARD"
    )


def test_sort():
    # Standard
    assert sort(10, 10, 10, 5) == "STANDARD"
    # Bulky only (volume)
    assert sort(200, 10, 10, 5) == "SPECIAL"
    # Bulky only (dimension)
    assert sort(10, 10, 151, 5) == "SPECIAL"
    # Heavy only
    assert sort(10, 10, 10, 25) == "SPECIAL"
    # Both bulky and heavy
    assert sort(200, 200, 200, 25) == "REJECTED"
    # Edge cases
    assert sort(150, 10, 10, 19.99) == "SPECIAL"
    assert sort(10, 10, 10, 20) == "SPECIAL"
    assert sort(150, 10, 10, 20) == "REJECTED"
    print("All tests passed.")

if __name__ == "__main__":
    test_sort()
