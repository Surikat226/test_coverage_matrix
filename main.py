import os
import pandas as pd

from helpers.data_collection import PrepareData
from helpers.output_file_styling import ExcelStyling
from helpers.data_collection import allure_reports_dir, sheet_name

from data.output_file_styling_data import Colors

data = PrepareData()
output_dir_name = 'output'
output_filename = 'coverage_matrix.xlsx'
output_file_path = os.path.join(output_dir_name, output_filename)

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
    # TODO Рзнести логику по функциям, чтобы было не так громоздко и стало читабельно
    test_matrix_info = data.collect_test_data(allure_reports_dir)

    indexes, cols, cell_values, cell_positions, tc_links = [], [], [], [], []

    for i in range(len(test_matrix_info)):
        # В качестве имени строки (индекса) делаем id + имя теста
        index = f"#{test_matrix_info[i]['test_id']} {test_matrix_info[i]['test_name']} {test_matrix_info[i]['test_param_summary']}"
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

    os.makedirs(output_dir_name, exist_ok=True)
    df.to_excel(output_file_path, sheet_name=sheet_name)

    styling = ExcelStyling(output_file_path=output_file_path)
    styling.align_cells_horizontally()
    styling.color_cells_by_test_results()
    styling.set_column_width()


if __name__ == '__main__':
    main()
