"""

Домашнее задание №2

Работа csv

* Создайте список словарей с ключами name, age и job
* Запишите содержимое списка словарей в файл в формате csv

"""
import csv

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    people = [
        {'name': 'John', 'age': 34, 'job': 'Analytic'},
        {'name': 'Sergei', 'age': 28, 'job': 'Lawyer'},
        {'name': 'Julia', 'age': 24, 'job': 'Psychologist'},
        {'name': 'Anna', 'age': 46, 'job': 'Designer'},
    ]
    with open('people.csv', 'w') as people_file:
        fieldnames = ['name', 'age', 'job']
        writer = csv.DictWriter(people_file, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(people)

if __name__ == "__main__":
    main()
