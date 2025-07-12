def is_valid_renavam(renavam):  # type: (str) -> bool
    """
    Validates the Brazilian vehicle registration number (RENAVAM).

    This function takes a RENAVAM string and checks if it is valid. 
    A valid RENAVAM consists of exactly 11 digits, with the last digit as 
    a verification digit calculated from the previous 10 digits.

    Args:
        renavam (str): The RENAVAM string to be validated.

    Returns:
        bool: True if the RENAVAM is valid, False otherwise.

    Example:
        >>> is_valid_renavam('12345678901')
        True
        >>> is_valid_renavam('12345678900')
        False
        >>> is_valid_renavam('1234567890a')
        False
        >>> is_valid_renavam('12345678 901')
        False
        >>> is_valid_renavam('12345678')  # Less than 11 digits
        False
        >>> is_valid_renavam('')  # Empty string
        False
    """

    if not renavam or not isinstance(renavam, str):
        return False
    
    renavam = renavam.strip()
    if not renavam.isdigit() or len(renavam) != 11:
        return False

    corpo = renavam[:10]
    digito_real = int(renavam[-1])

    corpo_invertido = list(map(int, reversed(corpo)))

    pesos = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3]
    soma = sum(d * p for d, p in zip(corpo_invertido, pesos))

    resto = soma % 11
    digito_calculado = 11 - resto if resto != 0 else 0
    if digito_calculado >= 10:
        digito_calculado = 0

    return digito_calculado == digito_real

    
