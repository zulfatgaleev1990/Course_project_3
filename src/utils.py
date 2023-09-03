import json
from src.funcs import file_sort
from src.funcs import operation_last_5

# Открываем json.файл и создаем список дат
with open("src/operations.json", "r", encoding="utf-8") as file:
    operations = json.load(file)
    list_date = []
    for operation in operations:
        if len(operation) != 0:
            list_date.append(operation.get('date'))

# Сортируем, фильтруем
list_operation = file_sort(list_date, operations)

# Выбираем первые пять
list_5 = list_operation[:5]

# Выводим на экран в определеннном формате
operation_last_5(list_5)

