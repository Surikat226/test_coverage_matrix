from tabulate import tabulate
from tests_data import TestsData

data = TestsData()

"""
Концепция:
1. Сбор информации о тестах из json-файлов отчётов
2. Матчинг этой информации с общей информацией обо всех существующих участках сервисов
3. Подготовка информации о покрытии функционала (распределение собранной информации о тестах по различным участкам
сервисов - какие участки были покрыты, какие нет, какие тесты прошли, а какие нет, а также разные ссылки на ТК и пр.)
4. Формирование матрицы покрытия
"""


def main():
    test_matrix_info = data.collect_test_data()
    table = tabulate(
        tabular_data=test_matrix_info,
        headers=['Наименование теста', 'ID', 'Статус', 'Ссылка на тест-кейс']
    )
    with open('coverage_matrix.txt', 'w', encoding='utf-8') as file:
        file.write(table)
    print(table)


if __name__ == '__main__':
    main()
