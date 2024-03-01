'''
Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя
логирование
'''

import os
import logging
from collections import namedtuple
import argparse

logging.basicConfig(filename='info.log', level=logging.INFO)
parser = argparse.ArgumentParser(description='Get info about files and directories')
parser.add_argument('path', type=str, help='Path to directory')
args = parser.parse_args()


def get_info(path):
    logging.info('Start')
    logging.info(f'Path: {path}')
    logging.info('Get info')
    info = []
    for root, dirs, files in os.walk(path):
        for file in files:
            name, ext = os.path.splitext(file)
            info.append(namedtuple('Object', ['name', 'ext', 'flag', 'parent'])
                        (name, ext, False, root))
        for directory in dirs:
            info.append(namedtuple('Object', ['name', 'ext', 'flag', 'parent'])
                        (directory, '', True, root))
    logging.info('Info collected')
    logging.info('Write to file')
    with open('info.txt', 'w') as file:
        for item in info:
            file.write(f'{item.name} {item.ext} {item.flag} {item.parent}\n')
    logging.info('End of work')


if __name__ == '__main__':
    get_info(args.path)
