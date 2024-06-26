def multiply_numbers(input_value=None):
    if not input_value:
        return None
    if isinstance(input_value, list):
        product = 1
        for item in input_value:
            product *= item
        return product
    elif isinstance(input_value, (int, float, str)):
        def digs(s):
            return [int(digit) for digit in str(s) if digit.isdigit()]

        digits = digs(input_value)
        if digits:
            product = 1
            for digit in digits:
                product *= digit
            return product
        else:
            return None


print(multiply_numbers())
