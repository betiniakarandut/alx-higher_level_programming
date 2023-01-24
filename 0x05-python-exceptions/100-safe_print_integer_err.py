#!\usr\bin\python3


def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format().

    Args:
        value (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    import sys
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as error:
        sys.stderr.write("Exception: {}\n".format(error))
        return False
