def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты.

    Args:
        card_number: Номер карты (16 цифр)

    Returns:
        str: Маскированный номер в формате XXXX XX** **** XXXX

    Example:
        >>> get_mask_card_number("1234567812345678")
        '1234 56** **** 5678'
    """
    # Удаляем все нецифровые символы
    digits = "".join(filter(str.isdigit, card_number))

    if len(digits) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    # Форматируем: XXXX XX** **** XXXX
    return f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета.

    Args:
        account_number: Номер счета

    Returns:
        str: Маскированный номер в формате **XXXX
        (где XXXX - последние 4 цифры)

    Example:
        >>> get_mask_account("1234567890123456")
        '**3456'
    """
    # Удаляем все нецифровые символы
    digits = "".join(filter(str.isdigit, account_number))

    if len(digits) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 цифры")

    # Маскируем: оставляем видимыми последние 4 цифры
    return f"**{digits[-4:]}"
