# TODO импортировать необходимые молули
from json import dump
from csv import DictReader

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
 # TODO считать содержимое csv файла
    with open(INPUT_FILENAME) as f:
        reader = DictReader(f)
        a = [i for i in reader]
    with open(OUTPUT_FILENAME, 'w') as ff:
        return dump(a, ff, indent=4)
  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
