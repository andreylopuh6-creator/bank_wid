"""Модуль виджета для работы с банковскими операциями."""

from .masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """ Маскирует номер карты или счета в строке с информацией о банковском продукте.

    Args:
        account_info: Строка с информацией о карте или счете
                     (например: "Visa Platinum 7000792289606361", "Счет 73654108430135874305")

    Returns:
        Строка с замаскированным номером карты или счета
    """
    if not account_info:
        return""

        # Разделяем строку на части
        parts = account_info.split()

        if len(parts) < 2:
            return account_info

        # Извлекаем номер (последняя часть строки)
        number = parts[-1]

        # Извлекаем название продукта (все части кроме последней)
        product_name = " ".join(parts[:-1])

        # Определяем тип продукта и применяем соответствующую маскировку
        if product_name.lower() == "счет" or "счет" in product_name.lower():
            masked_number = get_mask_account(number)
        else:
            # Для карт проверяем, что номер состоит из 16 цифр
            clean_number = number.replace(" ", "")
            if clean_number.isdigit() and len(clean_number) == 16:
                masked_number = get_mask_card_number(number)
            else:
                masked_number = number  # Если номер невалидный, возвращаем как есть

        return f"{product_name} {masked_number}"

    def get_date(date_string: str) -> str:
        """
        Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ.

        Args:
            date_string: Дата в формате "2024-03-11T02:26:18.671407"

        Returns:
            Дата в формате "11.03.2024"
        """
        if not date_string or "T" not in date_string:
            return date_string

        # Разделяем дату и время
        date_part = date_string.split("T")[0]

        # Разделяем год, месяц и день
        try:
            year, month, day = date_part.split("-")
            return f"{day}.{month}.{year}"
        except ValueError:
            return date_string



