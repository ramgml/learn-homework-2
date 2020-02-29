"""

Домашнее задание №2

Работа с файлами


* Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
* Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
* Подсчитайте количество слов в тексте
* Замените точки в тексте на восклицательные знаки
* Сохраните результат в файл referat2.txt
"""
import re


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('referat.txt', 'r') as referat_file:
        file_text = referat_file.read()

    print(f'Длина текста: {len(file_text)}')

    words = file_text.split()
    print(f'Количество слов: {len(words)}')

    changed_text = file_text.replace('.', '!')

    with open('referat2.txt', 'w') as referat_file:
        referat_file.write(changed_text)


if __name__ == "__main__":
    main()
