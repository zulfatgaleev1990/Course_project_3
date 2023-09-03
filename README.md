# Course project

Это третья курсовая работа в рамках обучения на курсах SkyPro. Проект направлен на обработку данных, представленных в формате JSON, которые представляют собой записи о банковских операциях с различными параметрами, такими как дата, статус, валюта, сумма и участники. Основная цель проекта - разработать программу, которая выводит информацию о последних пяти выполненных операциях, а также обеспечивает маскировку конфиденциальных данных.

## Функциональность

Программа предоставляет следующую функциональность:

- Загрузка данных из JSON-файла.
- Форматирование даты операции и вывод описания.
- Маскирование номеров карт и счетов для обеспечения анонимности данных.
- Отображение суммы операции в человеко-читаемом формате с указанием валюты.
- Вывод на экран информации о последних пяти выполненных операциях.

## Установка и использование

1. Склонируйте репозиторий на свой компьютер:

git clone https://github.com/zulfatgaleev1990/Course_project.git
markdown
2. Перейдите в директорию проекта:

cd Course_project
markdown
3. Запустите программу:

python main.py
markdown
Программа автоматически загрузит данные из JSON-файла и выведет информацию о последних пяти выполненных операциях, а также маскированные данные о плательщиках.

## Преимущества

- Программа обрабатывает данные о банковских операциях и предоставляет информацию о последних выполненных операциях.
- Данные о плательщиках анонимизированы для обеспечения конфиденциальности.
- Все функции покрыты тестами, обеспечивая надежность и корректную работу.

## Возможные улучшения

- Добавление обработки исключений для предотвращения сбоев при чтении данных из файлов и выполнении операций с датами.
- Улучшение алгоритма маскирования данных для более гибкой обработки различных форматов номеров карт и счетов.
- Расширение функциональности для работы с данными о банковских клиентах, а не только операциях.

## Автор

Зульфат Галеев  

## Лицензия

Этот проект лицензирован в соответствии с условиями MIT Licens
