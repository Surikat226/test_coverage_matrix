import pandas as pd
from helpers.data_collection import PrepareData
from helpers.output_file_styling import ExcelStyling
from helpers.data_collection import allure_reports_dir, sheet_name

data = PrepareData()
matrix_filename = 'output/coverage_matrix.xlsx'
styling = ExcelStyling(filename=matrix_filename)

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

    indexes, cols, cell_values, cell_positions, tc_links = [], [], [], [], []

    for i in range(len(test_matrix_info)):
        # В качестве имени строки (индекса) делаем id + имя теста
        index = f"#{test_matrix_info[i]['test_id']} {test_matrix_info[i]['test_name']}"
        indexes.append(index)

        # В качестве имени колонки делаем фичу теста
        col = test_matrix_info[i]['test_ierarchy'][0]['test_feature']
        if col not in cols:
            cols.append(col)

        cell_values.append(test_matrix_info[i]['test_status'])
        tc_links.append(test_matrix_info[i]['test_link'])

        cell_positions.append([index, col])

    df = pd.DataFrame(
        index=indexes,
        columns=cols
    )
    for i in range(len(cell_positions)):
        df.loc[*cell_positions[i]] = cell_values[i]

    df.to_excel(matrix_filename, sheet_name=sheet_name)

    styling.align_cells_horizontally()
    print(indexes)


if __name__ == '__main__':
    main()
