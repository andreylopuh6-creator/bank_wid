# Bank Operations

Утилиты для маскирования банковских реквизитов.

## Функциональность

- Маскирование номеров счетов
- Маскирование номеров банковских карт
- Фильтрация операций по статусу
- Сортировка операций по дате
- Написано на Python 3.13+
- Полное покрытие тестами

## Установка

```bash
# Установка в режиме разработки
pip install -e .

# Или обычная установка (если публикуете в PyPI)
pip install bank-operations
```

## Быстрый старт

```python
# Маскирование номера карты
card = "1234567812345678"
masked_card = get_mask_card_number(card)
print(f"Карта: {masked_card}")  # Карта: 1234 56** **** 5678

# Фильтрация операций по статусу
operations = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2024-01-10'},
    {'id': 2, 'state': 'CANCELED', 'date': '2024-01-15'},
]
executed = filter_by_state(operations)  # Только EXECUTED

# Сортировка операций по дате
sorted_ops = sort_by_date(operations)  # Сначала новые8
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
│   ├── __init__.py
│   ├── masks.py           
│   ├── processing.py      
│   ├── widget.py          
│   └── main.py            
├── tests/                  
│   ├── __init__.py
│   ├── test_masks.py
│   ├── test_processing.py
│   └── test_widget.py
├── .flake8                 
├── .gitignore
├── poetry.lock
├── pyproject.toml          
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

MIT License. 