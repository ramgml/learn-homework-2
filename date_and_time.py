"""

Домашнее задание №2

Дата и время

* Напечатайте в консоль даты: вчера, сегодня, месяц назад
* Превратите строку "01/01/17 12:10:03.234567" в объект datetime

"""
import calendar
from datetime import datetime, date, timedelta


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(date.today() - timedelta(days=1))
    print(date.today())

    today = date.today()
    month = 12 if today.month - 1 < 1 else today.month - 1
    year = today.year - 1 if today.month - 1 < 1 else today.year
    day = min(today.day, calendar.monthrange(year, month)[1])

    print(date(year, month, day))


def str_2_datetime(string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    return datetime.strptime(string, '%d/%m/%y %I:%M:%S.%f')


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/17 12:10:03.234567"))
