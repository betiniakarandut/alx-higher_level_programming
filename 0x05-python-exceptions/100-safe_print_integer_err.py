#!\usr\bin\python3


def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format().

    Args:
        value (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as ve:
        sys.stderr.write("Exception: {}\n".format(ve.args[0]))
        return False
