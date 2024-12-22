from tabulate import tabulate
from tests_data import TestsData

data = TestsData()


def main():
    test_matrix_info = data.collect_test_data()
    table = tabulate(
        tabular_data=test_matrix_info,
        headers=['Наименование теста', 'Статус']
    )
    with open('coverage_matrix.txt', 'w', encoding='utf-8') as file:
        file.write(table)
    print(table)


if __name__ == '__main__':
    main()
