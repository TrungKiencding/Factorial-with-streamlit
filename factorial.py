def factorial(value):
    """
    This function calculate the factorial for input value
    parameter of function is value you want to calculate factorial
    """

    if value == 0 or value == 1:
        return 1
    else:
        return value * factorial(value - 1)