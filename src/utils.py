import json
from datetime import datetime
import os

def file_reads():
    '''
    Функция, читающая и возвращающая данные
    '''
    with open(os.path.join('src', 'operations.json'), "r", encoding="utf-8") as file:
        operations = json.load(file)
        return operations

def empty_dict_filter(operations):
    '''
    Функция, фильтрующая пустые словари
    '''
    list_date = []
    for operation in operations:
        if len(operation) != 0:
            list_date.append(operation.get('date'))
    return list_date


def converter(text):
    '''
    Функция, маскирующая номер карты или счета звездочками
    '''
    number = []
    symbols = []
    for letter in text:
        if letter.isdigit():
            number.append(letter)
        if not letter.isdigit():
            symbols.append(letter)

    if len(number) == 20:
        return f"{''.join(symbols)}**{''.join(number[16:])}"
    elif len(number) == 16:
        return f"{''.join(symbols)}{''.join(number[:4])} {''.join(number[4:6])}** **** {''.join(number[12:16])}"


def file_sort(data, operations):
    '''
    Функция, возвращающая, фильтрующая успешные операции и сортирующая (в обратном направлении)
    '''
    list_sort = sorted(data, reverse=True)
    list_operation = []
    for date_ in list_sort:
        for operation in operations:
            if operation.get('date') == date_ and operation.get('state') != 'CANCELED':
                list_operation.append(operation)
    return list_operation


def operation_last_5(data):
    '''
    Функция, выводящая 5 последних выполненных клиентом операций в определеннном формате
    '''
    for operation in data:
        date_ = datetime.strptime(operation.get('date'), '%Y-%m-%dT%H:%M:%S.%f')
        if operation.get('description') != "Открытие вклада":
            print(f'''{date_.date().strftime('%d.%m.%Y')} {operation['description']}
{converter(operation.get('from', ""))} -> {operation.get('to')}
{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']} \n''')
        else:
            print(f'''{date_.date().strftime('%d.%m.%Y')} {operation['description']}
{operation.get('to')}
{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']} \n''')
