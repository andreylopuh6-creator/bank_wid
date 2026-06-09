# Bank Operations Processor

Утилиты для маскирования банковских реквизитов, фильтрации и сортировки банковских операций.

## Описание проекта

Проект предоставляет набор утилит для работы с банковскими данными:

- **Маскирование** номеров карт и счетов для безопасного отображения
- **Фильтрация** списка операций по статусу (EXECUTED, CANCELED, PENDING)
- **Сортировка** операций по дате (от новых к старым или наоборот)

Все функции имеют полную типизацию (аннотации типов) и расширенную документацию (docstring).

## Функциональность

### Модуль masks.py
- `get_mask_card_number(card_number: str) -> str` - маскирует номер банковской карты
- `get_mask_account(account_number: str) -> str` - маскирует номер счета

### Модуль processing.py
- `filter_by_state(data: List[Dict], state: str = 'EXECUTED') -> List[Dict]` - фильтрация операций по статусу
- `sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]` - сортировка операций по дате

## Зависимости

### Основные требования
- Python 3.13 или выше
- Стандартная библиотека Python (дополнительные пакеты не требуются)

### Зависимости для разработки

| Инструмент | Версия | Назначение |
|------------|--------|-------------|
| flake8     | >=7.0.0 | Проверка стиля кода (PEP 8) |
| mypy       | >=1.8.0 | Статическая проверка типов |
| unittest   | встроенный | Модульное тестирование |

## Установка и настройка

### 1. Клонирование репозитория

```bash
git clone <url-вашего-репозитория>
cd bankOP
2. Создание виртуального окружения
bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
3. Установка проекта
bash
# Установка в режиме разработки (рекомендуется)
pip install -e .

# Или обычная установка
pip install .
4. Установка инструментов для проверки кода
bash
pip install flake8 mypy
Использование
Пример 1: Маскирование карты и счета
python
from src.masks import get_mask_card_number, get_mask_account

# Маскирование карты
card_number = "1234567812345678"
masked_card = get_mask_card_number(card_number)
print(f"Карта: {masked_card}")  # Карта: 1234 56** **** 5678

# Маскирование счета
account_number = "12345678901234567890"
masked_account = get_mask_account(account_number)
print(f"Счет: {masked_account}")  # Счет: **7890
Пример 2: Фильтрация операций по статусу
python
from src.processing import filter_by_state

operations = [
    {"id": 1, "state": "EXECUTED", "amount": 1000, "date": "2024-01-10"},
    {"id": 2, "state": "CANCELED", "amount": 500, "date": "2024-01-15"},
    {"id": 3, "state": "EXECUTED", "amount": 750, "date": "2024-01-20"}
]

# Фильтрация по умолчанию (статус 'EXECUTED')
executed_ops = filter_by_state(operations)
print(executed_ops)
# Вывод: [{"id": 1, ...}, {"id": 3, ...}]

# Фильтрация с указанием статуса
canceled_ops = filter_by_state(operations, "CANCELED")
print(canceled_ops)
# Вывод: [{"id": 2, ...}]
Пример 3: Сортировка операций по дате
python
from src.processing import sort_by_date

operations = [
    {"id": 1, "date": "2024-01-15T10:00:00"},
    {"id": 2, "date": "2024-01-10T14:30:00"},
    {"id": 3, "date": "2024-01-20T09:15:00"}
]

# Сортировка от новых к старым (по умолчанию)
newest_first = sort_by_date(operations)
print(newest_first)
# Вывод: {"id": 3}, {"id": 1}, {"id": 2}

# Сортировка от старых к новым
oldest_first = sort_by_date(operations, reverse=False)
print(oldest_first)
# Вывод: {"id": 2}, {"id": 1}, {"id": 3}
Проверка качества кода
Запуск тестов
bash
# Запуск всех тестов
python -m unittest discover tests

# Запуск с подробным выводом
python -m unittest discover tests -v

# Запуск конкретного тестового файла
python -m unittest tests.test_processing

# Запуск конкретного теста
python -m unittest tests.test_processing.TestProcessing.test_filter_by_state
Проверка стиля кода (flake8)
bash
# Проверка всех файлов
flake8 src tests

# Проверка с дополнительными параметрами
flake8 src tests --max-line-length=88 --count --statistics

# Проверка конкретного файла
flake8 src/processing.py
Проверка типов (mypy)
bash
# Проверка всех файлов
mypy src --ignore-missing-imports

# Проверка конкретного файла
mypy src/processing.py --ignore-missing-imports
Ожидаемые результаты
Проверка	Успешный результат
flake8	Отсутствие вывода (нет ошибок)
mypy	Success: no issues found in X source files
unittest	OK (все тесты пройдены)
Структура проекта
text
bankOP/
├── src/
│   ├── __init__.py
│   ├── masks.py          # Маскирование карт и счетов
│   ├── processing.py     # Фильтрация и сортировка операций
│   ├── widget.py         # Дополнительные утилиты
│   └── main.py           # Точка входа
├── tests/
│   ├── __init__.py
│   ├── test_masks.py     # Тесты для masks.py
│   ├── test_processing.py # Тесты для processing.py
│   └── test_widget.py    # Тесты для widget.py
├── .flake8               # Конфигурация flake8
├── .gitignore
├── poetry.lock
├── pyproject.toml        # Конфигурация проекта
└── README.md
Конфигурационные файлы
.flake8
ini
[flake8]
max-line-length = 88
exclude = venv,__pycache__,docs
count = true
statistics = true
pyproject.toml (для mypy)
toml
[tool.mypy]
ignore_missing_imports = true
exclude = ["venv/", "tests/"]
Возможные проблемы и решения
Ошибка "FileNotFoundError: processing.py"
Решение: Убедитесь, что вы находитесь в правильной директории:

bash
cd src
flake8 processing.py
Ошибка импорта при запуске тестов
Решение: Установите проект в режиме разработки:

bash
pip install -e .
mypy не находит модули
Решение: Используйте флаг --ignore-missing-imports:

bash
mypy src --ignore-missing-imports
Лицензия
MIT License