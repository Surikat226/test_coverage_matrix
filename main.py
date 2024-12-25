import pandas as pd
from helpers.data_collection import PrepareData
from helpers.output_file_styling import align_cells_horizontally
from helpers.data_collection import allure_reports_dir, sheet_name

data = PrepareData()
matrix_filename = 'output/coverage_matrix.xlsx'


"""
Концепция:
1. Сбор информации о тестах из json-файлов отчётов
2. Матчинг этой информации с общей информацией обо всех существующих участках сервисов
3. Подготовка информации о покрытии функционала (распределение собранной информации о тестах по различным участкам
сервисов - какие участки были покрыты, какие нет, какие тесты прошли, а какие нет, а также разные ссылки на ТК и пр.)
4. Формирование матрицы покрытия

Обработка некорректных/неожиданных данных:
1. Не найдена директория с отчётами - рейзить соответствующую ошибку
2. Не найден тот или иной ключ в тестах из allure-reports - рейзить ошибку или отдавать None. Если отдавать None, то 
корректно его вставлять в таблицу
"""


def main():
    test_matrix_info = data.collect_test_data(allure_reports_dir)

    df_data_massive, indexes, tc_links = list(), list(), list()

    for i in range(len(test_matrix_info)):
        df_data_massive.append(test_matrix_info[i]['test_status'])
        indexes.append(f"#{test_matrix_info[i]['test_id']} {test_matrix_info[i]['test_name']}")
        tc_links.append(test_matrix_info[i]['test_link'])

    df = pd.DataFrame(
        df_data_massive,
        index=indexes
    )
    df.to_excel(matrix_filename, sheet_name=sheet_name)

    align_cells_horizontally(filename=matrix_filename)


if __name__ == '__main__':
    main()
