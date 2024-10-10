from datetime import date
from typing import Optional
from babel.dates import format_date


def int_to_digit_list(number) -> list[int]:
    """
    Converts an integer into a list of its individual digits.

    Args:
    number (int): The integer to be converted.

    Returns:
    list[int]: A list containing individual digits of the input number.

    Example:
    >>> int_to_digit_list(12345)
    [1, 2, 3, 4, 5]
    """
    number_str = str(number)
    return [int(digit) for digit in number_str]


def return_gender_from_pesel(number: int):
    """
    Determines the gender based on the PESEL number.

    Args:
    number (int): PESEL number as an integer.

    Returns:
    str: "żeńska" (female) if the gender is female, "męska" (male) if the gender is male.

    Note:
    The function uses the 10th digit of the PESEL number to determine the gender.
    Even digits indicate female, odd digits indicate male.
    """
    digits = int_to_digit_list(number)
    gender_digit = digits[9]
    if gender_digit % 2 == 0:
        return "żeńska"
    else:
        return "męska"


def return_birth_date_from_pesel(number: int) -> Optional[date]:
    """
    Extracts and formats the birth date from a PESEL number.

    Args:
    number (int): PESEL number as an integer.

    Returns:
    Optional[date]: Formatted birth date string in Polish locale if valid,
                    or an error message string if the date is invalid.

    Note:
    - Handles different centuries (1900s, 2000s, 2100s) based on the month value.
    - Returns a formatted date string using Polish locale.
    - If the date is invalid, it returns an error message instead.
    """
    digits = int_to_digit_list(number)
    digits = digits[:6]

    year = digits[0] * 10 + digits[1]
    month = digits[2] * 10 + digits[3]
    day = digits[4] * 10 + digits[5]

    if month > 32:
        month -= 40
        year += 2100
    elif month > 12:
        month -= 20
        year += 2000
    else:
        year += 1900

    try:
        birth_date = date(year, month, day)

        return format_date(birth_date, locale='pl_PL')
    except ValueError as e:
        print(f"Invalid date: {e}")
        return f"Invalid date: {e}"


def validate_number(number: int) -> bool:
    """
    Validates a PESEL number using the check digit algorithm.

    Args:
    number (int): PESEL number to be validated.

    Returns:
    bool: True if the PESEL number is valid, False otherwise.

    Note:
    The function uses a specific algorithm with weight multipliers [1, 3, 7, 9]
    to calculate the check digit and compare it with the control sum.
    """
    digits = int_to_digit_list(number)

    control_sum = digits[-1]
    total_sum = 0
    multipliers = [1, 3, 7, 9]

    for i, digit in enumerate(digits[:10]):
        mnoznik = multipliers[i % len(multipliers)]
        total_sum += digit * mnoznik

    check_digit = total_sum % 10
    validation_digit = (10 - check_digit) % 10

    if validation_digit == control_sum:
        return True
    else:
        return False
