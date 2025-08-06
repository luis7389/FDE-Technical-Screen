# Package Sorting Automation

This project provides a Python function to sort packages for robotic automation according to their volume and mass, following Thoughtful's robotic automation factory rules.

## Features
- Classifies packages as `STANDARD`, `SPECIAL`, or `REJECTED` based on size and weight.
- Includes comprehensive test coverage for all edge cases.

## Usage

1. Clone or download this repository.
2. (Optional) Create a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Run the script to execute tests:
   ```powershell
   python sort_packages.py
   ```

## Function Reference

```
def sort(width, height, length, mass):
    """
    Sorts a package into the correct stack based on its dimensions and mass.
    Returns: 'STANDARD', 'SPECIAL', or 'REJECTED'.
    """
```

## Test Coverage
The script includes a `test_sort()` function with assertions for all required scenarios and edge cases. Running the script will print `All tests passed.` if everything is correct.


