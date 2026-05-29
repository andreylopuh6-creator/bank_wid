"""Главный модуль функции."""

from masks import get_mask_account, get_mask_card_number


def main() -> None:
    """Демонстрация функции маскировки."""
    # Примеры использования
    card_numbers = [
        "1234567890123456",
        "1111222233334444",
        "5555666677778888",
    ]

    account_numbers = [
        "1234567890",
        "1111222233334444",
        "73654108430105874305",
    ]

    print("Примеры маскировки номеров карт:")
    for card in card_numbers:
        try:
            masked = get_mask_card_number(card)
            print(f"Оригинал: {card} -> Замаскированный: {masked}")
        except ValueError as e:
            print(f"Ошибка с картой {card}: {e}")

    print("\nПримеры маскировки номеров счетов:")
    for account in account_numbers:
        try:
            masked = get_mask_account(account)
            print(f"Оригинал: {account} -> Замаскированный: {masked}")
        except ValueError as e:
            print(f"Ошибка со счетом {account}: {e}")

    print("\nДемонстрация завершена!")


if __name__ == "__main__":
    main()