# Bank Operations

Утилиты для маскирования банковских реквизитов.

## Функциональность

- Маскирование номеров счетов
- Маскирование номеров банковских карт
- Написано на Python 3.8+
Полное покрытие тестами

## Установка

```bash
# Установка в режиме разработки
pip install -e .

# Или обычная установка (если публикуете в PyPI)
pip install bank-operations
```

## Быстрый старт

```python
from src.masks import mask_account_number, mask_card_number

# Маскирование номера счета
account = "123456789012"
masked_account = mask_account_number(account)
print(f"Счет: {masked_account}")  # Счет: **9012

# Маскирование номера карты
card = "1234567812345678"
masked_card = mask_card_number(card)
print(f"Карта: {masked_card}")  # Карта: 1234 56** **** 5678
```

## Тестирование

```bash
# Запуск всех тестов
python -m unittest discover tests

# Запуск с подробным выводом
python -m unittest discover tests -v

# Запуск конкретного теста
python -m unittest tests.test_masks.TestMasks.test_mask_account_number
```

## Структура проекта

```
bank_operations/
├── src/
│   └── masks/
│       ├── __init__.py
│       └── masks.py
├── tests/
│   ├── __init__.py
│   └── test_masks.py
├── pyproject.toml
├── .flake8
└── README.md
```

## Разработка

1. Клонируйте репозиторий
2. Установите зависимости:
```bash
pip install -e .[dev]
```

3. Запустите тесты:
```bash
python -m unittest discover tests
```

4. Проверьте стиль кода:
```bash
flake8 src tests
```

## Лицензия

MIT License. Смотрите LICENSE файл для деталей.