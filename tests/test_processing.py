from src.processing import filter_by_state, sort_by_date

# Наши тестовые данные
test_data = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
    {'id': 2, 'state': 'CANCELED', 'date': '2023-01-02'},
    {'id': 3, 'state': 'EXECUTED', 'date': '2023-01-03'},
    {'id': 4, 'state': 'PENDING', 'date': '2023-01-04'},
]

print("Проверка filter_by_state (должны быть операции с id 1 и 3):")
result = filter_by_state(test_data)
for item in result:
    print(f"  id: {item['id']}, state: {item['state']}")

print("\nПроверка filter_by_state со статусом CANCELED (должна быть операция с id 2):")
result = filter_by_state(test_data, 'CANCELED')
for item in result:
    print(f"  id: {item['id']}, state: {item['state']}")

print("\nПроверка sort_by_date (должны идти от новых к старым: 4,3,2,1):")
result = sort_by_date(test_data)
for item in result:
    print(f"  id: {item['id']}, date: {item['date']}")